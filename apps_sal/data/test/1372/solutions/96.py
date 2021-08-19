import numpy as np
(h, n) = list(map(int, input().split()))
ab = np.array([list(map(int, input().split())) for _ in range(n)])
dp = np.zeros(10 ** 4 + 1, np.int64)
dp[0] = 0
for (a, b) in ab:
    dp[1:a + 1] = np.minimum(dp[1:a + 1], b)
for i in range(1, h + 1):
    dp[i] = np.min(dp[i - ab[:, 0]] + ab[:, 1])
print(dp[h])
