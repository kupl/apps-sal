# coding: utf-8
import sys
import numpy as np
from collections import Counter


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


MOD = 10 ** 9 + 7
# 素因数分解をして、それぞれの因数をどこに入れるか


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


U = 10 ** 5 + 100  # 階乗テーブルの上限
fact, fact_inv = make_fact(U, MOD)


def prime_factorize(n):  # Nの素因数分解
    A = []
    while n % 2 == 0:
        A.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            A.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        A.append(n)
    return A


N, M = lr()
primes = prime_factorize(M)
counter = Counter(primes)
answer = 1
for v in list(counter.values()):
    cases = cmb(N - 1 + v, v)
    answer *= cases
    answer %= MOD

print((answer % MOD))
# np.int64とint型の違いに注意
# 16
