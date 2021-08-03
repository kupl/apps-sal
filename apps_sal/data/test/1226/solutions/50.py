import functools
import operator

n, a, b = list(map(int, input().split()))


def nCr(n, r):
    r = min(r, n - r)
    if r == 0:
        return 1
    num = functools.reduce(lambda x, y: x * y % mod, list(range(n, n - r, -1)))
    den = functools.reduce(lambda x, y: x * y % mod, [pow(x, mod - 2, mod) for x in range(1, r + 1)])
    return num * den % mod


mod = 10**9 + 7
print(((pow(2, n, mod) - nCr(n, a) - nCr(n, b) - 1) % mod))
