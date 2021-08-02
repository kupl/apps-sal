import functools
import operator


def nCr(n, r):
    if n < r:
        return 0
    r = min(r, n - r)
    if r == 0:
        return 1
    num = functools.reduce(operator.mul, range(n, n - r, -1))
    den = functools.reduce(operator.mul, range(1, r + 1))
    return num // den % mod


n, k = map(int, input().split())

mod = 10**9 + 7
for i in range(1, k + 1):
    print(nCr(k - 1, i - 1) * nCr(n - k + 1, i) % mod)
