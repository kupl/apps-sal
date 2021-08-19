from heapq import heappush, heappop
from math import inf
import numpy as np
n = int(input())
A = []
[heappush(A, (-v, i)) for (i, v) in enumerate(map(int, input().split()), 1)]
dp = np.full((n + 1, n + 1), -inf, dtype=int)
dp[0, 0] = 0
for i in range(n):
    (v, j) = heappop(A)
    v = -v
    dp[i + 1, 1:] = dp[i, :-1] + v * np.abs(j - np.arange(1, n + 1))
    dp[i + 1, :-1] = np.maximum(dp[i, :-1] + v * np.abs(j - np.arange(n - i, n + n - i)), dp[i + 1, :-1])
print(dp[-1, ].max())
