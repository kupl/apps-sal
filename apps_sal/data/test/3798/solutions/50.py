from functools import reduce
from collections import Counter
from itertools import product
import operator
from math import sqrt, ceil


def bisect(ng, ok, judge, eps=1):
    while abs(ng - ok) > eps:
        m = (ng + ok) // 2
        if judge(m):
            ok = m
        else:
            ng = m
    return ok


int_product = lambda it: reduce(operator.mul, it, 1)

# 素因数分解


def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            yield i
    if n > 1:
        yield n

# 約数列挙


def divisors(n):
    fac_pow = Counter(prime_factors(n))
    fac = tuple(fac_pow.keys())
    for pp in product(*(range(p + 1) for p in fac_pow.values())):
        yield int_product(f**p for f, p in zip(fac, pp))


def f(x, b):
    cnt = 0
    while x:
        cnt += x % b
        x //= b
    return cnt


def solve(n, s):
    if n == s:
        return n + 1
    if n < s:
        return -1
    for b in range(2, ceil(sqrt(n)) + 2):
        if f(n, b) == s:
            return b
    for d in sorted(divisors(n - s)):
        b = d + 1
        if f(n, b) == s:
            return b
    return -1


n = int(input())
s = int(input())
print(solve(n, s))
