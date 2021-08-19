import numpy as np
(n, s) = list(map(int, input().split()))
a = list(map(int, input().split()))
mod = 998244353
res = 0
dp = np.zeros(s + 1, dtype=int)
for i in range(n):
    dp[0] += 1
    dp[a[i]:] += dp[:-a[i]].copy()
    dp %= mod
    res += dp[s]
    res %= mod
print(res)
