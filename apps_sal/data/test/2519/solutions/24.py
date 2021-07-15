def rsum(n):return (n+1)*(n//2)+((n+1)//2) if n%2 else (n+1)*(n//2)
N,K=map(int,input().split())
p=list(map(int,input().split()))
l=[0]*N
for i in range(N):l[i]=rsum(p[i])*(1/p[i])
s=sum(l[0:K])
ans=0
for i in range(N-K):
    ans=max(ans,s)
    s-=l[i]
    s+=l[i+K]
print(max(ans,s))
