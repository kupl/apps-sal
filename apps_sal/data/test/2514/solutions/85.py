N=int(input())
A=list(map(int,input().split()))
cnt=[0 for _ in range(100001)]
for i in range(N):
    cnt[A[i]]+=1
ans=sum(A)
Q=int(input())
for _ in range(Q):
    B,C=map(int,input().split())
    cnt[C]+=cnt[B]
    ans+=(C-B)*cnt[B]
    cnt[B]=0
    print(ans)
