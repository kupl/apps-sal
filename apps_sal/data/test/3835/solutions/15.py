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
    n, m = map(int, input().split())
    return n, m


def dva():
    n, m = map(int, input().split())
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
    return(ret)


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


def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans


n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    if i == 0:
        x = i + 1
        j = i + 2
        tc1 = a[i][x]
        tc2 = a[i][j]
        print(int((tc1 * tc2 // a[x][j]) ** 0.5), end=' ')
    elif i == n - 1:
        x = i - 1
        j = i - 2
        tc1 = a[i][x]
        tc2 = a[i][j]
        print(int((tc1 * tc2 // a[x][j]) ** 0.5), end=' ')
    else:
        x = 0
        j = n - 1
        tc1 = a[i][x]
        tc2 = a[i][j]
        print(int((tc1 * tc2 // a[x][j]) ** 0.5), end=' ')
