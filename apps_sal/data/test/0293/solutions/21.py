from itertools import chain, combinations
from functools import reduce
from collections import defaultdict


def res(m, n):
    k = min(m, n)
    return (1 + k) * (k + 2 * k ** 2 - 3 * k * (m + n) + 6 * m * n) // 6


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable((combinations(s, r) for r in range(len(s) + 1)))


def prod(it):
    r = 1
    for elem in it:
        r *= elem
    return r


def factorGenerator(n):
    res = defaultdict(lambda: 0)
    for p in range(2, 10 ** 6 + 1):
        while n % p == 0:
            res[p] += 1
            n = n // p
    return res


def divisorGen(n):
    factors = list(factorGenerator(n).items())
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x * y, [factors[x][0] ** f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return


def res2(x):
    r = []
    x6 = 6 * x
    divisors = set(divisorGen(x6))
    for m in divisors:
        a = x6 // m
        if a % (m + 1) != 0:
            continue
        b = a // (m + 1)
        c = b + m - 1
        if c % 3 != 0:
            continue
        n = c // 3
        if n < m:
            continue
        if res(m, n) != x:
            continue
        r.append((m, n))
    return r


x = int(input())
r = res2(x)
r = r + [(n, m) for (m, n) in r]
r = sorted(set(r))
print(len(r))
for (m, n) in r:
    print('%d %d' % (m, n))
