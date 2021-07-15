import numpy as np

S = input()
mod = int(10**9 + 7)
dp = np.zeros(13, dtype=int)
dp[0] = 1

M = np.zeros((13, 13), dtype=int)
for i in range(13):
    for d in range(10):
        M[i][(i * 10 + d) % 13] += 1

for s in S:
    ndp = np.zeros(13, dtype=int)
    if s == '?':
        ndp = np.dot(dp, M)
    else:
        d = int(s)
        for j in range(13):
            ndp[(j * 10 + d) % 13] += dp[j]
    dp = ndp % mod

print(dp[5])
