import math
from decimal import Decimal
import heapq


def na():
    n = int(input())
    b = [int(x) for x in input().split()]
    return n, b


def nab():
    n = int(input())
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    return n, b, c


def dv():
    n, m = list(map(int, input().split()))
    return n, m


def dva():
    n, m = list(map(int, input().split()))
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    return n, m, b


def eratosthenes(n):
    sieve = list(range(n + 1))
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sorted(set(sieve))


def nm():
    n = int(input())
    b = [int(x) for x in input().split()]
    m = int(input())
    c = [int(x) for x in input().split()]
    return n, b, m, c


def dvs():
    n = int(input())
    m = int(input())
    return n, m


n, m = list(map(int, input().split()))
a = []
for i in range(n):
    s = input()
    a.append(s)
b = list(map(int, input().split()))
ans = 0
for j in range(m):
    d = {}
    for i in range(n):
        c = a[i][j]
        d[c] = d.get(c, 0) + 1
    tc = max(d.values()) * b[j]
    ans += tc
print(ans)
