import numpy as np

N, M = list(map(int, input().split()))
S = tuple(map(int, input().split()))
T = np.array(input().split(), np.int64)
mod = 10 ** 9 + 7

dp = np.ones(M + 1, np.int64)
for i in S:
    tmp = (T == i)
    dp[1:] = (np.cumsum(tmp * dp[:-1]) + dp[1:]) % mod

print((dp[-1]))

