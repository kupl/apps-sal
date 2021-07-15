n,k=map(int,input().split())
mod=998244353
M=[]
for i in range(k):
    l,r=map(int,input().split())
    M.append([l,r])

dp=[0]*(3*n)
dp[0]=1
dp[1]=-1
#imos
for i in range(n):
    for l,r in M:
        dp[l+i]+=dp[i]
        dp[i+r+1]-=dp[i]
    dp[i+1]=(dp[i]+dp[i+1])%mod
print(dp[n-1])
