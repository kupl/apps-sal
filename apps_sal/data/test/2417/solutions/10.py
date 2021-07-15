import sys
input = sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

inda=0
indb=0
ANS=0
USE=[0]*(n+1)

while inda<n and indb<n:
    NOW=A[inda]
    USE[A[inda]]=1

    for i in range(indb,n):
        if B[i]==NOW:
            break
        else:
            if USE[B[i]]==0:
                ANS+=1
                USE[B[i]]=1

    indb=i+1
    
    while inda<n and USE[A[inda]]==1:
        inda+=1

    #print(inda,indb,ANS)

print(ANS)

