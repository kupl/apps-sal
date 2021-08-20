import math
from operator import mul
from functools import reduce
(n, m, k) = map(int, input().split())
mod = 998244353


def cmb(n, r, p):
    if r < 0 or n < r:
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
for i in range(2, n + 1):
    fact.append(fact[-1] * i % mod)
    inv.append(-inv[mod % i] * (mod // i) % mod)
    factinv.append(factinv[-1] * inv[-1] % mod)
ans = 0
for i in range(k + 1):
    ans += m * cmb(n - 1, i, mod) * pow(m - 1, n - 1 - i, mod) % mod
    ans %= mod
print(ans)
