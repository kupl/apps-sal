from operator import mul
from functools import reduce


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


def mult(a, b):
    return (a * b) % mod


n, m, k = map(int, input().split())
mod = 998244353
ans = 1
ans = mult(ans, (m - 1)**k)
ans = mult(ans, m)
ans = mult(ans, ncr(n - 1, k))

print(ans)
