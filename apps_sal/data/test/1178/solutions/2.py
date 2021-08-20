import numpy as np
(n, k) = map(int, input().split())
h = np.array(input().split(), dtype=np.int)
if k < n:
    dp = np.zeros((n - k, n), dtype=np.int)
    dp[0] = h
    for i in range(n - k - 1):
        for j in range(i + 1, n):
            dp[i + 1, j] = np.min(dp[i][i:j] + np.maximum(h[j] - h[i:j], 0))
    print(dp[n - k - 1, n - k - 1:].min())
else:
    print(0)
