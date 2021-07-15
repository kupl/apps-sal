import numpy as np

mod = 998244353
n, s = map(int, input().split())
dp = np.zeros(s+1, dtype=int)
dp[0] = 1
for a in map(int, input().split()):
  pre_dp = dp
  dp = pre_dp * 2 % mod
  dp[a:] = (dp[a:] + pre_dp[:-a]) % mod
print(dp[-1])
