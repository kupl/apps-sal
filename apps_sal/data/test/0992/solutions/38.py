import numpy as np

mod = 998244353
n, s = map(int, input().split())
dp = np.zeros((n+1, s+1), dtype=int)
dp[0, 0] = 1
for i, a in enumerate(map(int, input().split())):
  dp[i+1] = dp[i] * 2 % mod
  dp[i+1][a:] = (dp[i+1][a:] + dp[i][:-a]) % mod
print(dp[-1, -1])
