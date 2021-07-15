MOD=10**9+7
N=int(input())

dp=[[0 for _ in range(3)] for _ in range(64)]
dp[63][0]=1

for d in range(62,-1,-1):
  b=(N>>d)&1 
  s=dp[d+1][:]
  dp[d][0]=dp[d+1][0]+(1^b)*dp[d+1][1] % MOD
  dp[d][1]=b*dp[d+1][0]+dp[d+1][1] % MOD
  dp[d][2]=(1+b)*dp[d+1][1]+3*dp[d+1][2] % MOD

print(sum(dp[0][:]) % MOD)
