
# -*- coding: UTF-8 -*-

import sys


def get_ints():
    return list(map(int, sys.stdin.readline().strip().split()))


def mul(x, y, mod):
    x %= mod
    y %= mod
    return x * y % mod


def div(x, y, mod):
    x %= mod
    y %= mod
    return x * mod_pow(y, mod - 2, mod) % mod


def mod_pow(a, p, mod):
    if p == 0:
        return 1
    if p % 2 == 0:
        root = mod_pow(a, p / 2, mod)
        return root * root % mod
    else:
        return a * mod_pow(a, p - 1, mod) % mod


def pre_factorial_divs(n, mod, factorials):
    factorial_divs = [0] * (n + 1)

    factorial_divs[n] = div(1, factorials, mod)
    for i in reversed(list(range(n))):
        factorial_divs[i] = mul(factorial_divs[i + 1], i + 1, mod)
    return factorial_divs


def pre_factorials(n, mod):
    factorials = [0] * (n + 1)
    factorials[0] = 1
    for i in range(n):
        factorials[i + 1] = (i + 1) * factorials[i] % mod
    return factorials


def fast_fast_fermat_comb(a, b, mod, factorials, factorial_divs):
    if len(factorials) == 0:
        raise
    af = factorials[a]
    bf = factorial_divs[b]
    abf = factorial_divs[a - b]
    return mul(mul(af, bf, mod), abf, mod)


def main():
    h, w, a, b = get_ints()

    ans = 0
    mod = 10 ** 9 + 7

    factorials = pre_factorials(h + w - 2, mod)
    factorial_divs = pre_factorial_divs(h + w - 2, mod, factorials[h + w - 2])

    for i in range(h - a):
        x = fast_fast_fermat_comb(b - 1 + i, b - 1, mod, factorials, factorial_divs)
        y = fast_fast_fermat_comb(h + w - 3 - (b - 1 + i), w - b - 1, mod, factorials, factorial_divs)
        ans += x * y % mod
        ans %= mod

    print(ans)


def __starting_point():
    main()


__starting_point()
