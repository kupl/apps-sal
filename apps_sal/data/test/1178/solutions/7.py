import numpy as np
(N, K) = map(int, input().split())
H = list(map(int, input().split()))
sortedH = np.hstack((np.zeros(1, dtype=np.int64), np.sort(H)))
dic = {}
for (i, h) in enumerate(sortedH):
    dic[h] = i
inf = 10 ** 15
dp = np.full((302, len(sortedH) + 1), inf, dtype=np.int64)
dp[0, 0] = 0
for (i, h) in enumerate(H):
    for k in range(i + 1, -1, -1):
        dp[k + 1] = np.minimum(dp[k + 1], dp[k])
        idx = dic[h]
        ma = np.min(dp[k][:idx] + h - sortedH[:idx])
        mb = np.min(dp[k][idx:])
        dp[k] = np.full(len(sortedH) + 1, inf, dtype=np.int64)
        dp[k][idx] = min(ma, mb)
print(np.min(dp[:K + 1]))
