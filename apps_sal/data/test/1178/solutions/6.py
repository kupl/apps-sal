import numpy as np
(n, k) = list(map(int, input().split()))
hhh = list(map(int, input().split()))
hhh = np.array([0] + hhh, dtype=np.int64)
INF = 10 ** 18
dp = np.full((n + 1, k + 1), fill_value=INF, dtype=np.int64)
dp[0, 0] = 0
for (i, h) in enumerate(hhh[1:], start=1):
    ndp = np.full((n + 1, k + 1), fill_value=INF, dtype=np.int64)
    ndp[:n, 1:] = dp[:n, :-1]
    ndp[i] = (dp + np.maximum(0, h - hhh)[:, np.newaxis]).min(axis=0)
    dp = ndp
print(dp.min())
