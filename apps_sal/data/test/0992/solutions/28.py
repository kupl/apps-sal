import numpy as np
n, s = map(int, input().split())
*a, = map(int, input().split())
l = min(s + 1, 3001)
dp = np.zeros(l, dtype=int)
dp[0] = 1
mod = 998244353
ans = 0
cnt = 0
for ai in a:
    dp2 = dp[:-ai].copy()
    dp *= 2
    dp[ai:] += dp2
    dp %= mod
print(dp[s])
