import collections
import math
from operator import mul
from functools import reduce
(N, M) = list(map(int, input().split()))


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, list(range(n, n - r, -1)), 1)
    denom = reduce(mul, list(range(1, r + 1)), 1)
    return numer // denom


c = collections.Counter(prime_factorize(M))
primeFactorizeList = list(c.values())
answer = 1
for i in primeFactorizeList:
    answer *= combinations_count(i + N - 1, i)
    answer = answer % (10 ** 9 + 7)
print(int(answer))
