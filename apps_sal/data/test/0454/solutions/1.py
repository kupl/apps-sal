import numpy as np
n, k = map(int, input().split())
m = n**2
mod = 10**9+7
dp = np.zeros((n+1, n+1, m+1), dtype=np.int64)
dp[0,0,0] = 1
for i in range(1, n+1):
  for j in range(i+1):
    dp[i,j,2*j:] = (2*j+1)*dp[i-1,j,:m+1-2*j]
    if j+1 <= i-1:
      dp[i,j,2*j:] += (j+1)*(j+1)*dp[i-1,j+1,:m+1-2*j]
    if j:
      dp[i,j,2*j:] += dp[i-1,j-1,:m+1-2*j]
    dp[i,j,2*j:] %= mod
ans = dp[n,0,k]
print(ans)
