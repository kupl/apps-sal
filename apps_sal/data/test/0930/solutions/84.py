# coding: utf-8
import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

MOD = 10 ** 9 + 7
# K回の移動が終わった後、人がいる部屋の数はNからN-K

def cmb(n, k):
    if k < 0 or k > n: return 0
    return fact[n] * fact_inv[k] % MOD * fact_inv[n-k] % MOD

def cumprod(arr, MOD):
    L = len(arr); Lsq = int(L**.5+1)
    arr = np.resize(arr, Lsq**2).reshape(Lsq, Lsq)
    for n in range(1, Lsq):
        arr[:, n] *= arr[:, n-1]; arr[:, n] %= MOD
    for n in range(1, Lsq):
        arr[n] *= arr[n-1, -1]; arr[n] %= MOD
    return arr.ravel()[:L]

def make_fact(U, MOD):
    x = np.arange(U, dtype=np.int64); x[0] = 1
    fact = cumprod(x, MOD)
    x = np.arange(U, 0, -1, dtype=np.int64); x[0] = pow(int(fact[-1]), MOD-2, MOD)
    fact_inv = cumprod(x, MOD)[::-1]
    return fact, fact_inv

U = 10 ** 6  # 階乗テーブルの上限
fact, fact_inv = make_fact(U, MOD)

N, K = lr()
answer = 0
for x in range(N, max(0, N-K-1), -1):
    # x個の家には1人以上いるのでこの人たちは除く
    can_move = N - x
    # x-1の壁をcan_move+1の場所に入れる
    answer += cmb(N, x) * cmb(x - 1 + can_move, can_move)
    answer %= MOD
    
print((answer % MOD))
# 31

