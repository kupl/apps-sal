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
    elif p == 3:
        return list(input())
    else:
        return int(input())


n, x, y = f(1)
s = f(3)

count = 0

for i in range(n - x, n):
    if (s[i] == '1' and i != n - 1 - y) or (s[i] == '0' and i == n - 1 - y):
        count += 1

print(count)
