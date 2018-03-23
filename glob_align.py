import numpy as np

def get_matrix(seq1,seq2,gap,mismatch,match):
    m = len(seq1)+1
    n = len(seq2)+1
    best_matrix=np.zeros(shape=(m,n),dtype = int)
    zhizhen=np.zeros(shape=(m,n),dtype = int)
    #initialize
    for i in range(1,m):
        best_matrix[i,0] = best_matrix[i-1,0]+ gap
        zhizhen[i,0] = 1 #top
    for j in range(1,n):
        best_matrix[0,j] = best_matrix[0,j-1]+ gap
        zhizhen[0,j] = 2 #left
        
    for i in range(1,m):
        for j in range(1,n):
            num1 = best_matrix[i-1,j] + gap
            num2 = best_matrix[i,j-1] + gap
            if  seq1[i-1] == seq2[j-1]:
                num3 = best_matrix[i-1,j-1] + match
            else:
                num3 = best_matrix[i-1,j-1] + mismatch
            max1=max(num1,num2,num3)
            best_matrix[i,j] = max1
            if max1 == num1:
                zhizhen[i,j] = 1  #top
            if max1 == num2:
                zhizhen[i,j] = 2 #left
            if max1 == num3:
                zhizhen[i,j] = 3  #diag        
                
    print "score:"+ str(best_matrix[m-1,n-1])
    
    return best_matrix,zhizhen

def get_path(zhizhen,seq1,seq2):
    r1 = []
    r2 = []
    m = len(seq1)
    n = len(seq2)
    while m != 0 or n != 0:
        
        if zhizhen[m,n] == 1:
            move = "top"
        elif zhizhen[m,n] ==2:
            move = "left"
        elif zhizhen[m,n] == 3:
            move = "diag"
        if move == "diag":
            r1.append(seq1[m-1])
            r2.append(seq2[n-1])
            m -=1
            n -=1
        if move == "top":
            r1.append(seq1[m-1])
            r2.append("-")
            m -=1
        if move == "left":
            r1.append("-")
            r2.append(seq2[n-1])
            n -=1
    s1="".join(r1)[::-1]
    s2="".join(r2)[::-1]
    
    return s1,s2

if __name__== "__main__":
    gap=-1
    mismatch=-1
    match=1
    seq1="aattgccgccgtcgttttcagcagttatgtcagatc"
    seq2="tcccagttatgtcaggggacacgagcatgcagagac"
    (best_matrix,zhizhen) =get_matrix(seq1,seq2,gap,mismatch,match)                                      
    (s1,s2)=get_path(zhizhen,seq1,seq2)
    print s1
    print s2
