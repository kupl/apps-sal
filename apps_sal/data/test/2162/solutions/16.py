import math
from decimal import Decimal
import heapq
from collections import deque


def na():
    n = int(input())
    b = [int(x) for x in input().split()]
    return (n, b)


def nab():
    n = int(input())
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    return (n, b, c)


def dv():
    (n, m) = list(map(int, input().split()))
    return (n, m)


def dva():
    (n, m) = list(map(int, input().split()))
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    return (n, m, b)


def eratosthenes(n):
    sieve = list(range(n + 1))
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sorted(set(sieve))


def lol(lst, k):
    k = k % len(lst)
    ret = [0] * len(lst)
    for i in range(len(lst)):
        if i + k < len(lst) and i + k >= 0:
            ret[i] = lst[i + k]
        if i + k >= len(lst):
            ret[i] = lst[i + k - len(lst)]
        if i + k < 0:
            ret[i] = lst[i + k + len(lst)]
    return ret


def nm():
    n = int(input())
    b = [int(x) for x in input().split()]
    m = int(input())
    c = [int(x) for x in input().split()]
    return (n, b, m, c)


def dvs():
    n = int(input())
    m = int(input())
    return (n, m)


def fact(a, b):
    c = []
    ans = 0
    f = int(math.sqrt(a))
    for i in range(1, f + 1):
        if a % i == 0:
            c.append(i)
    l = len(c)
    for i in range(l):
        c.append(a // c[i])
    for i in range(len(c)):
        if c[i] <= b:
            ans += 1
    if a / f == f and b >= f:
        return ans - 1
    return ans


(k1, k2, k3) = list(map(int, input().split()))
n = k1 + k2 + k3
a = [-1] * n
x1 = list(map(int, input().split()))
x2 = list(map(int, input().split()))
x3 = list(map(int, input().split()))
for i in x1:
    a[i - 1] = 0
for i in x2:
    a[i - 1] = 1
for i in x3:
    a[i - 1] = 2
ans = k1 + k2
mx = 0
cntl = [0] * 3
cntr = [0] * 3
for i in range(n):
    cntr[a[i]] += 1
for i in range(n):
    cntl[a[i]] += 1
    cntr[a[i]] -= 1
    mx = max(mx, cntl[0] - cntl[1])
    tc = cntr[0] + cntr[1] + cntl[2] + cntl[0] - mx
    ans = min(ans, tc)
print(ans)
