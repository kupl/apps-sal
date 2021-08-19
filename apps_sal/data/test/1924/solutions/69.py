# coding: utf-8
import sys
import numpy as np


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


MOD = 10 ** 9 + 7


def cmb(n, k):
    if k < 0 or k > n:
        return 0
    return fact[n] * fact_inv[k] % MOD * fact_inv[n - k] % MOD


def cumprod(arr, MOD):
    L = len(arr)
    Lsq = int(L**.5 + 1)
    arr = np.resize(arr, Lsq**2).reshape(Lsq, Lsq)
    for n in range(1, Lsq):
        arr[:, n] *= arr[:, n - 1]
        arr[:, n] %= MOD
    for n in range(1, Lsq):
        arr[n] *= arr[n - 1, -1]
        arr[n] %= MOD
    return arr.ravel()[:L]


def make_fact(U, MOD):
    x = np.arange(U, dtype=np.int64)
    x[0] = 1
    fact = cumprod(x, MOD)
    x = np.arange(U, 0, -1, dtype=np.int64)
    x[0] = pow(int(fact[-1]), MOD - 2, MOD)
    fact_inv = cumprod(x, MOD)[::-1]
    return fact, fact_inv


U = 2 * 10 ** 6 + 3  # 階乗テーブルの上限
fact, fact_inv = make_fact(U, MOD)

r1, c1, r2, c2 = lr()
answer = cmb(r2 + c2 + 2, r2 + 1) - 1
answer -= cmb(r2 + c1 + 1, r2 + 1) - 1
answer -= cmb(r1 + c2 + 1, c2 + 1) - 1
answer += cmb(r1 + c1, r1) - 1
print((answer % MOD))
# 26
