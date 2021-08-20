import numpy as np
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
(N, K) = map(int, input().split())
MOD = 10 ** 9 + 7
dp = np.zeros((N + 1, N * N + 1), dtype=np.int64)
dp[0, 0] = 1
for n in range(1, N + 1):
    prev = dp
    dp = np.zeros_like(prev)
    for m in range(N):
        dp[m, m:] += prev[m, :N * N + 1 - m]
        dp[m, m:] += prev[m, :N * N + 1 - m] * m
        dp[m + 1, m + 1:] += (m + 1) * prev[m, :N * N - m]
        dp[m, m:] += prev[m, :N * N + 1 - m] * m
        dp[m, m:] += (m + 1) * prev[m + 1, :N * N + 1 - m]
    dp %= MOD
if K & 1:
    answer = 0
else:
    answer = dp[0, K // 2]
print(answer)
