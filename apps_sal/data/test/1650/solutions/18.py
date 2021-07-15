L=input()
N=len(L)
dp=[[0,0]for _ in range(N)]
dp[0][0]=1
dp[0][1]=2
mod=10**9+7
for i in range(1,N):
  dp[i][0]+=3*dp[i-1][0]
  dp[i][0]%=mod
  if L[i]=='0':
    dp[i][1]+=dp[i-1][1]
  else:
    dp[i][0]+=dp[i-1][1]
    dp[i][1]+=dp[i-1][1]*2
  dp[i][0]%=mod
  dp[i][1]%=mod
print(sum(dp[-1])%mod)
