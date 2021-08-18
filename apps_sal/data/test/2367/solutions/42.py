import sys
from math import factorial

MOD = 10 ** 9 + 7


def combInit(n):
    fact = [1]
    finv = [1]
    for i in range(1, n + 1):
        fact.append(fact[i - 1] * i % MOD)
        finv.append(pow(fact[i], MOD - 2, MOD))
    return [fact, finv]


def comb(n, k, f):
    if n < k:
        return 0
    elif n < 0 or k < 0:
        return 0
    else:
        return f[0][n] * (f[1][k] * f[1][n - k] % MOD) % MOD


def perm(n, r):
    return factorial(n) // factorial(r)


def gcb(a, b):
    if b == 0:
        return a
    else:
        return gcb(b, a % b)


def lcm(a, b):
    d = gcb(a, b)
    return int(a / d * b)


def surP(x):
    return x % MOD


def main():
    h, w, a, b = list(map(int, input().split()))

    f = combInit(h + w)
    res = 0
    for i in range(b, w):
        res += comb((h - 1 - a) + i, i, f) * comb((a - 1) + (w - 1 - i), w - 1 - i, f)

    out = surP(res)
    print(("{}".format(out)))


def __starting_point():
    main()


__starting_point()
