#!/usr/bin/env python3
import sys
from math import gcd, sqrt


def rint():
    return list(map(int, sys.stdin.readline().split()))


def find_prime_factors(num):
    d = set()
    i = 2
    while i < int(sqrt(num) + 1):
        while num % i == 0:
            d.add(i)
            num = num // i
        i += 1
    if num > 1:
        d.add(num)
    return d


n = int(input())

a, b = rint()

pf = find_prime_factors(a).union(find_prime_factors(b))

for i in range(n - 1):
    a, b = rint()
    pftmp = pf.copy()
    for f in pf:
        if a % f and b % f:
            pftmp.remove(f)
    pf = pftmp.copy()

if len(pf):
    print(pf.pop())
else:
    print(-1)
