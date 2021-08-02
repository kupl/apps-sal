import math
import bisect
import heapq

from collections import defaultdict


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)


def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n


primes = []


def isprime(n):
    for d in range(2, int(math.sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True


def argsort(ls):
    return sorted(range(len(ls)), key=ls.__getitem__)


def f(p=0):
    if p == 1:
        return map(int, input().split())
    elif p == 2:
        return list(map(int, input().split()))
    else:
        return int(input())


n = f()
cl = f(2)

count = 0
sm = 0

for i in range(n):
    a = sm
    b = cl[i] // 2
    t = min(a, b)
    count += t
    sm += cl[i]
    cl[i] -= t * 2
    sm -= t * 3
    c = cl[i] // 3
    sm -= c * 3
    count += c

print(count)
