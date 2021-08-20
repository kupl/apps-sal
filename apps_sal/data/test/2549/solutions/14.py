import sys
from sys import stdin
import bisect


def inverse(a, mod):
    return pow(a, mod - 2, mod)


def modfac(n, MOD):
    f = 1
    factorials = [1]
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
    return (factorials, invs)


def modnCr(n, r):
    return fac[n] * inv[n - r] * inv[r] % mod


mod = 998244353
(fac, inv) = modfac(3 * 10 ** 5, mod)
(n, m) = list(map(int, stdin.readline().split()))
d = list(map(int, stdin.readline().split()))
d.sort()
dsum = sum(d)
s = [0]
for i in range(n):
    s.append(s[-1] + d[i])
aaa = []
for loop in range(m):
    (a, b) = list(map(int, stdin.readline().split()))
    X = bisect.bisect_left(d, b)
    Y = n - X
    xsum = s[X]
    ysum = dsum - xsum
    ans = 0
    if a <= Y:
        ans += ysum * fac[n] * (Y - a) * inverse(Y, mod)
        ans += xsum * fac[n] * (Y - a + 1) * inverse(Y + 1, mod)
        ans %= mod
    aaa.append(ans * inv[n] % mod)
print('\n'.join(map(str, aaa)))
