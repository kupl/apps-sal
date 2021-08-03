import sys
import numpy as np

N, M, Q = list(map(int, input().split(' ')))

dp = np.zeros(shape=(N + 1, N + 1), dtype=int)
for _ in range(M):
    L, R = list(map(int, input().split(' ')))
    dp[L][R] += 1

dp = dp.cumsum(axis=1).cumsum(axis=0)

queries = np.array(list(map(int, sys.stdin.read().split())))

left = queries[0::2] - 1
right = queries[1::2]

print(('\n'.join((dp[right, right] + dp[left, left] - dp[left, right] - dp[right, left]).astype(str))))
