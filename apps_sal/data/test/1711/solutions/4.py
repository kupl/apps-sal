import math
import collections
import sys
input = sys.stdin.readline


def ncr(n, r, p):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p


n, m = map(int, input().split())
mod = 998244353
if n == 2:
    print(0)
else:
    ans = ncr(m, n - 1, mod)
    ans *= (n - 2)
    ans %= mod
    ans *= pow(2, n - 3, mod)
    ans %= mod
    print(ans)
