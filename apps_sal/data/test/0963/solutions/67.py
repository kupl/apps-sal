mod = 998244353
n,k = list(map(int,input().split()))
lr = [list(map(int,input().split())) for _ in range(k)]
dp = [0]*(n+1)
dp[1] = 1
dpt = [0]*(n+1)
dpt[1] = 1
for i in range(1,n+1):
  for l,r in lr:
    if i-l>0:
      dp[i] += dpt[i-l]
      if i-r-1>0:
        dp[i] -= dpt[i-r-1]
  dp[i] %= mod
  dpt[i] = dpt[i-1]+dp[i]
  dpt[i] %= mod
print((dp[n]))

