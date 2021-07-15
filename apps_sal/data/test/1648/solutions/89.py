n,k=map(int,input().split())
dp=[[0]*(n+1) for _ in range(n+1)]
mod=10**9+7
dp[0][0]=1
dp[1][0]=1
dp[1][1]=1
for i in range(2,n+1):
    for j in range(n+1):
        dp[i][j]=(dp[i-1][j-1]+dp[i-1][j])%mod
for a in range(1,k+1):
    if n-k+1<a:
        print(0)
        continue
    else:
        print(dp[n-k+1][a]*dp[k-1][a-1]%mod)   
