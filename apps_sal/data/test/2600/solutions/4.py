import sys
input = sys.stdin.readline
from collections import Counter

t=int(input())
for tests in range(t):
    n,m=list(map(int,input().split()))
    M=[list(map(int,input().split())) for i in range(n)]

    A=[[] for i in range(n+m-1)]

    for i in range(n):
        for j in range(m):
            A[i+j].append(M[i][j])

    ANS=0

    for k in range((n+m-1)//2):
        C=Counter(A[k]+A[-k-1])
        ANS+=min(C[0],C[1])

    print(ANS)

    
    
    

