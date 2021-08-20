import sys
import numpy as np


def sr():
    return sys.stdin.readline().rstrip()


def ir():
    return int(sr())


def lr():
    return list(map(int, sr().split()))


MOD = 10 ** 9 + 7
(N, K) = lr()
M = int(N ** 0.5)
upper_cnt = np.zeros(M + 1, dtype=np.int64)
A = np.arange(M + 1, dtype=np.int64)
upper_cnt[1:] = N // A[1:] - np.maximum(M, N // (A[1:] + 1))
lower = np.zeros(M + 1, dtype=np.int64)
upper = np.zeros(M + 1, dtype=np.int64)
lower[1] = 1
for i in range(K):
    prev_lower = lower.copy()
    prev_upper = upper.copy()
    lower_cum = prev_lower.cumsum() % MOD
    upper_cum = prev_upper.cumsum() % MOD
    lower = np.zeros(M + 1, dtype=np.int64)
    lower[1:] += lower_cum[-1] + upper_cum[-1]
    lower[1:] -= upper_cum[:-1]
    upper = lower_cum * upper_cnt
    lower %= MOD
    upper %= MOD
answer = (lower[1:].sum() + upper[1:].sum()) % MOD
print(answer)
