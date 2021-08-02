import numpy as np
S = input()
M = 13
MOD = 10**9 + 7
dp = np.zeros(M, dtype=np.int64)
dp[0] = 1
idx = np.zeros(M, dtype=np.int8)
window = np.ones(10, dtype=np.int8)
for i in range(M):
    idx[i * 10 % M] = i
for s in S:
    if s == '?':
        tdp = dp[idx]
        ndp = np.concatenate([tdp[4:], tdp])
        dp = np.convolve(ndp, window, mode='valid') % MOD
    else:
        dp = np.roll(dp[idx], int(s))
print((dp[5] % MOD))
