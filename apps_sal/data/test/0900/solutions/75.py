import numpy as np


def solve(s):
    MOD = 10 ** 9 + 7
    dp = np.zeros(13, dtype=np.int64)
    dp[0] = 1
    idx = np.zeros(13, dtype=np.int8)
    for i in range(13):
        idx[i * 10 % 13] = i
    window = np.ones(10, dtype=np.int8)
    for c in s:
        if c == '?':
            tdp = dp[idx]
            ndp = np.concatenate([tdp[4:], tdp])
            dp = np.convolve(ndp, window, mode='valid') % MOD
        else:
            dp = np.roll(dp[idx], int(c))
    return dp[5]


s = input()
print((solve(s)))
