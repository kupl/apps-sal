N=int(input())
D,X=map(int,input().split())
A = [int(input()) for _ in range(N)]

B=[0]*N

for i in range(N):
    if D%A[i]!=0:
        for j in range(D//A[i]+1):
            B[i]=1+D//A[i]
    else:
        B[i]=D//A[i]
print(sum(B)+X)
