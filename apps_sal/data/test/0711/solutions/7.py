# coding: utf-8
from collections import Counter


def ncr(n, r, mod):
    ret = 1
    for i in range(1, r + 1):
        ret = (ret * (n - i + 1) * pow(i, mod - 2, mod)) % mod
    return ret


def solve(*args: str) -> str:
    n, m = list(map(int, args[0].split()))
    mod = 10**9 + 7
    C = Counter()

    i = 2
    r = -int(-m**(1 / 2) // 1)
    while 1 < m:
        while m % i == 0:
            C[i] += 1
            m //= i
        if r < i:
            C[m] = 1
            break
        i += 1

    ret = 1
    for v, c in list(C.items()):
        ret *= ncr(n + c - 1, min(n - 1, c), mod)
        ret %= mod

    return str(ret)


def __starting_point():
    print((solve(*(open(0).read().splitlines()))))


__starting_point()
