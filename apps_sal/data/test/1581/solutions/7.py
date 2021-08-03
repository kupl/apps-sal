# coding: utf-8
import sys
import numpy as np


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


# 桁dp、√Nまでをlower、それ以降をup_range、Nをlowerで割ったものでまとめる
MOD = 10 ** 9 + 7
N, K = lr()
M = int(N ** .5)
A = np.arange(M + 1, dtype=np.int64)
high_range = np.zeros(M + 1, dtype=np.int64)
high_range[1:] = N // A[1:] - np.maximum(M, N // (A[1:] + 1))  # Mはlowerに入れるので0
low = np.zeros(M + 1, dtype=np.int64)
high = np.zeros(M + 1, dtype=np.int64)
low[1] = 1
for _ in range(K):
    prev_low = low.copy()
    prev_high = high.copy()
    prev_low_cum = prev_low.cumsum() % MOD
    prev_high_cum = prev_high.cumsum() % MOD
    low = np.zeros(M + 1, dtype=np.int64)
    low[1:] += (prev_low_cum[-1] + prev_high_cum[-1])
    low[1:] -= prev_high_cum[:-1]
    high = prev_low_cum * high_range
    low %= MOD
    high %= MOD

answer = (low[1:].sum() + high[1:].sum()) % MOD
print((answer % MOD))
