import sys
input = sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))

if n<=3:
    X=0
    for a in A:
        X|=a
    print(X)

else:
    ANS=0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                ANS=max(ANS,A[i]|A[j]|A[k])

    print(ANS)

