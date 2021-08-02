import math
from decimal import Decimal


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
aa = [int(x) for x in input().split()]
l = {i: m for i in range(n)}
r = {i: -1 for i in range(n)}
for i, a in enumerate(aa):
    l[a - 1] = min(i, l[a - 1])
    r[a - 1] = max(i, r[a - 1])
ans = 0
for i in range(n):
    for j in range(3):
        a = i
        b = i + j - 1
        if b < 0 or b == n:
            continue
        if l[a] > r[b]:
            ans += 1
print(ans)
