import sys
from functools import lru_cache
sys.setrecursionlimit(10 ** 9)


def mul(x, y, mod):
    x %= mod
    y %= mod
    return x * y % mod


def div(x, y, mod):
    x %= mod
    y %= mod
    return x * mod_pow(y, mod - 2, mod) % mod


@lru_cache(maxsize=None)
def mod_pow(a, p, mod):
    if p == 0:
        return 1
    if p % 2 == 0:
        root = mod_pow(a, p / 2, mod)
        return root * root % mod
    else:
        return a * mod_pow(a, p - 1, mod) % mod


def dnm(n, mod, factorials):
    denominators = [0] * (n + 1)
    denominators[n] = div(1, factorials, mod)
    for i in reversed(range(n)):
        denominators[i] = mul(denominators[i + 1], i + 1, mod)
    return denominators


def nmr(n, mod):
    factorials = [0] * (n + 1)
    factorials[0] = 1
    for i in range(n):
        factorials[i + 1] = (i + 1) * factorials[i] % mod
    return factorials


def cmb(a, b, mod, factorials, factorial_divs):
    if len(factorials) == 0:
        raise
    af = factorials[a]
    bf = factorial_divs[b]
    abf = factorial_divs[a - b]
    return mul(mul(af, bf, mod), abf, mod)


MOD = 10 ** 9 + 7
(H, W, A, B) = map(int, input().split())
ans = 0
n = nmr(H + W - 2, MOD)
d = dnm(H + W - 2, MOD, n[H + W - 2])
for i in range(H - A):
    x = cmb(B - 1 + i, B - 1, MOD, n, d)
    y = cmb(H + W - 3 - (B - 1 + i), W - B - 1, MOD, n, d)
    ans += x * y % MOD
    ans %= MOD
print(ans)
