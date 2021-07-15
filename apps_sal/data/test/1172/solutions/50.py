import numpy as np

MOD = 10 ** 9 + 7

S = input()

n = len(S)
dp = np.zeros((n+1, 4), np.int64)
dp[0, 0] = 1
for i, c in enumerate(S):
    if c == 'A' or c == '?':
        dp[i+1] += dp[i]
        dp[i+1, 1] += dp[i, 0]
    if c == 'B' or c == '?':
        dp[i+1] += dp[i]
        dp[i+1, 2] += dp[i, 1]
    if c == 'C' or c == '?':
        dp[i+1] += dp[i]
        dp[i+1, 3] += dp[i, 2]
    dp[i+1] %= MOD

print((dp[n, 3]))


