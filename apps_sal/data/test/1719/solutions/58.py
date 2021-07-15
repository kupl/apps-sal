import numpy as np
from itertools import product

n = int(input())

mod = 10**9 + 7
A, G, C, T = list(range(1, 5))
dp = np.zeros((n+1, 5, 5, 5), dtype=np.int64)
dp[0, 0, 0, 0] = 1
for m in range(n):
    for i, j, k, l in product(list(range(5)), list(range(5)), list(range(5)), list(range(1, 5))):
        if i == A and j == G and l == C:
            continue
        if i == A and k == G and l == C:
            continue
        if j == A and k == G and l == C:
            continue
        if j == G and k == A and l == C:
            continue
        if j == A and k == C and l == G:
            continue
        dp[m+1, j, k, l] += dp[m, i, j, k]
        dp[m, i, j, k] %= mod

res = 0
for i, j, k in product(list(range(1, 5)), repeat=3):
    res += dp[n, i, j, k]
    res %= mod
print(res)

