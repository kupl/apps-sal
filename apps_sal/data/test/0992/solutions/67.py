import numpy as np
n, s = list(map(int, input().split()))
a = list(map(int, input().split()))
mod = 998244353
dp = np.zeros((n + 1, 3001), int)
dp[0][0] = 1

for i in range(n):
    dp[i + 1] += dp[i] * 2
    dp[i + 1, a[i]:] += dp[i, :-a[i]]
    dp[i + 1] %= mod
print((dp[n][s]))
