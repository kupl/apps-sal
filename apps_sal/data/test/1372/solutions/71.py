import numpy as np

h, n = list(map(int, input().split()))
m = np.array([list(map(int, input().split())) for _ in range(n)])

max_a = np.max(m[:, 0])
dp = np.zeros(h + max_a + 1, dtype='i8')
for i in range(max_a + 1, h + max_a + 1):
    dp[i] = np.min(dp[i - m[:, 0]] + m[:, 1])
print((dp[h + max_a]))
