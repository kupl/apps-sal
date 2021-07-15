n,k=list(map(int,input().split()))
mod=998244353
hee=[tuple(map(int,input().split())) for _ in range(k)]
dp=[0]*(n+1)
dp[1]=1
summdp=[0]*(n+1)
summdp[1]=1
for i in range(2,n+1):
    for l,r in hee:
        li=max(i-l,0)
        ri=max(i-r-1,0)
        dp[i]+=summdp[li]-summdp[ri]
        dp[i]%=mod
    summdp[i]=summdp[i-1]+dp[i]
print((dp[n]))


