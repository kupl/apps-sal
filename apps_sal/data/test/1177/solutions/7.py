N,S =list(map(int,input().split()))
A=list(map(int,input().split()))
mod=998244353
ans=0
q=[0]*(S+1)
for i in range(N):
    q2=q.copy()
    if A[i]<=S:
        for j in range(A[i],S+1):
            q[j]+=q2[j-A[i]]
        q[A[i]]+=i+1
    ans+=q[S]
    ans%=mod
print(ans)

