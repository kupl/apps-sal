from functools import *
from math import gcd
from collections import *


def isValid(n):
    if n <= 0:
        return 0
    if n - int(n) != 0:
        return 0
    return 1


def mu(n):
    if n == 1:
        return 1
    elif isDivisibleBySquare(n):
        return 0
    else:
        return (-1) ** numberOfFactors(n)


def isDivisibleBySquare(n):
    if n % 2 == 0:
        n = n / 2
    if n % 2 == 0:
        return True
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            n //= i
        if n % i == 0:
            return True
    return False


def factorGenerator(n):
    r = []
    while n % 2 == 0:
        n //= 2
        r.append(2)
    i = 3
    while i * i <= n:
        while n % i == 0:
            n //= i
            r.append(i)
        i += 2
    if n != 1:
        r.append(n)
    return r


def numberOfFactors(n):
    return len(factorGenerator(n))


def divisors(n):
    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


def calc(m, n):
    s = 0
    for d in sorted(list(set(divisors(n)))):
        s += mu(d) * (m // d)
    return s


n = int(input())
for _ in range(n):
    (a, m) = list(map(int, input().split()))
    g = gcd(a, m)
    print(calc((m + a - 1) // g, m // g) - calc((a - 1) // g, m // g))
