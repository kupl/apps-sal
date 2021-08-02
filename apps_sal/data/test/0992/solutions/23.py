import numpy as np
n, s = map(int, input().split())
a = [int(j)for j in input().split()]
dp = [0] * (3000 + 1)
dp[0] = 1
pre = np.array(dp)
mod = 998244353
for i in a:
    dp = pre * 2
    dp[i:] += pre[:-i]
    dp %= mod
    pre = dp
print(dp[s])
