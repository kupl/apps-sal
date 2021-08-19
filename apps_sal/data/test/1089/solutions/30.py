import numpy as np
import sys
sys.setrecursionlimit(10 ** 7)
(N, M, K) = list(map(int, input().split()))
ans = 0
MOD = 10 ** 9 + 7


def cumprod(arr, MOD):
    L = len(arr)
    Lsq = int(L ** 0.5 + 1)
    arr = np.resize(arr, Lsq ** 2).reshape(Lsq, Lsq)
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
    return (fact, fact_inv)


U = N * M + 10
(fact, fact_inv) = make_fact(U, MOD)
(fact, fact_inv) = (fact.tolist(), fact_inv.tolist())


def mod_comb_k(n, k, mod):
    return fact[n] * fact_inv[k] % mod * fact_inv[n - k] % mod


for dx in range(1, N):
    pat = N - dx
    ans += dx * pat * M * M
    ans %= MOD
for dy in range(1, M):
    pat = M - dy
    ans += dy * pat * N * N
    ans %= MOD
ans *= mod_comb_k(N * M - 2, K - 2, MOD)
ans %= MOD
print(ans)
