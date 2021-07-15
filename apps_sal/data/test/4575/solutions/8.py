N=int(input())
D,X=map(int,input().split())
A=[int(input()) for _ in range(N)]
for i in range(N):
    cnt=0
    while A[i]*cnt+1<=D:
        cnt+=1
    X+=cnt
print(X)
