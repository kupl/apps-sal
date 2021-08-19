import math
import operator as op
from functools import reduce
from operator import mul
from fractions import Fraction


def nCk(n, k):
    return int(reduce(mul, (Fraction(n - i, i + 1) for i in range(k)), 1))


def ncr(n, r):
    r = min(r, n - r)
    if r == 0:
        return 1
    numer = reduce(op.mul, list(range(n, n - r, -1)))
    denom = reduce(op.mul, list(range(1, r + 1)))
    return numer // denom


def modPow(a, x, p):
    res = 1
    while x > 0:
        if x % 2 != 0:
            res = res * a % p
        a = a * a % p
        x = int(x / 2)
    return res


def modInverse(a, p):
    return modPow(a, p - 2, p)


def modBinomial(n, k, p):
    numerator = 1
    for i in range(k):
        numerator = numerator * (n - i) % p
    denominator = 1
    for i in range(1, k + 1):
        denominator = denominator * i % p
    return numerator * modInverse(denominator, p) % p


(n, c) = input().split()
n = int(n)
c = int(c)
ans = modBinomial(c + n, c, 1000003) - 1
print(int(ans))
