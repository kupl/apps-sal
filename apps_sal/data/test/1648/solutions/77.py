#coding: utf-8
from collections import defaultdict
import sys


def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


p = 10 ** 9 + 7
N = 3000  # N は必要分だけ用意する
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

N, K = (int(i) for i in input().split())
for i in range(1, K + 1):
    ret = cmb(N - K + 1, i, p)
    ret %= p
    ret *= cmb(K - 1, i - 1, p)
    ret %= p
    print(ret)
