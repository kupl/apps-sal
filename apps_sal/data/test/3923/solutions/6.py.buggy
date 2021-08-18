#!/usr/bin/env python3

import sys

n, a, b = list(map(int, sys.stdin.readline().strip().split()))

# supposed a>=0, b>=0, a+b>0
# returns (d, p, q) where d = gcd(a, b) = a*p + b*q


def euc(a, b):
    if b > a:
        (d, p, q) = euc(b, a)
        return (d, q, p)
    if b == 0:
        return (a, 1, 0)
    s = a // b
    (d, sp, sq) = euc(a - s * b, b)
    return (d, sp, sq - s * sp)


def normalize(n, a, b, d, p, q):
    if p < 0:
        (sp, sq) = normalize(n, b, a, d, q, p)
        return (sq, sp)
    elif q >= 0:
        return (p, q)
    # p>=0, q < 0
    r = - (q // (a // d))
    sp = p - r * (b // d)
    sq = q + r * (a // d)
    if sp < 0:
        raise ValueError
    else:
        return (sp, sq)


(d, p, q) = euc(a, b)
if n % d != 0:
    print('-1')
    return
m = n // d
p, q = m * p, m * q
try:
    (p, q) = normalize(n, a, b, d, p, q)
except ValueError:
    print('-1')
    return

res = []
last = 1
for _ in range(p):
    res.extend(list(range(last + 1, last + a)))
    res.append(last)
    last += a
for _ in range(q):
    res.extend(list(range(last + 1, last + b)))
    res.append(last)
    last += b

print(' '.join(map(str, res)))
