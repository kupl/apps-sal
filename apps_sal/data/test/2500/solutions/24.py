N = int(input())
MOD = 10**9+7
dp = [[0]*3 for _ in range(61)]
dp[60][0] = 1
for d in range(59,-1,-1):
  for s in range(3):
    for k in range(3):
      ns = min(2, 2*s + ((N>>d)&1) - k)
      if ns < 0:
        continue
      dp[d][ns] += dp[d+1][s]
      dp[d][ns] %= MOD

print(sum(dp[0])%MOD)
