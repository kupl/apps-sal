import sys
import numpy as np

sys.setrecursionlimit(10 ** 7)

r1, c1, r2, c2 = list(map(int, input().split()))


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


MOD = 10 ** 9 + 7
U = 10**6 * 2 + 10
fact, fact_inv = make_fact(U, MOD)


def mod_comb_k(n, k, mod):
    return fact[n] * fact_inv[k] % mod * fact_inv[n - k] % mod


def calc_rc(r, c):
    a = mod_comb_k(r + c + 2, r + 1, MOD)
    b = 1
    return a - b


ans = calc_rc(r2, c2) + calc_rc(r1 - 1, c1 - 1) - \
    calc_rc(r1 - 1, c2) - calc_rc(r2, c1 - 1)
ans %= MOD

print(ans)
