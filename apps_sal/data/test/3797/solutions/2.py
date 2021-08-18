from collections import defaultdict
import numpy as np
import sys
input = sys.stdin.readline


MOD = 10 ** 9 + 7
N, M = map(int, input().split())
LRX = [[int(x) for x in input().split()] for _ in range(M)]

R_to_LX = defaultdict(list)
for l, r, x in LRX:
    R_to_LX[r].append((l, x))

for n in range(1, N + 1):
    if n == 1:
        dp = np.zeros((n, n), dtype=np.int64)
        dp[0, 0] = 1
    else:
        prev = dp
        dp = np.zeros((n, n), dtype=np.int64)
        dp[:-1, :-1] = prev
        dp[n - 1, :-1] = prev.sum(axis=0)
        dp[:-1, n - 1] = prev.sum(axis=1)
    for l, x in R_to_LX[n]:
        if x == 1:
            dp[l:, :] = 0
            dp[:, l:] = 0
        elif x == 2:
            dp[l:, l:] = 0
            dp[:l, :l] = 0
        elif x == 3:
            dp[:l, :] = 0
            dp[:, :l] = 0
    dp %= MOD

answer = dp.sum() * 3 % MOD
print(answer)
