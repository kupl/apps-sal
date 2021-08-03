import math
from decimal import Decimal
import heapq
import copy
import heapq
from collections import deque


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


def da():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    return n, m, a


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


def fact(n):
    tc = []
    ans = {}
    d = 2
    while d * d <= n:
        if n % d == 0:
            tc.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        tc.append(n)
    for i in tc:
        ans[i] = ans.get(i, 0) + 1
    return ans


for i in range(int(input())):
    n, a = na()
    nech = 0
    s = 0
    for j in a:
        if j % 2 == 1:
            nech += 1
        s += j
    if s % 2 == 1:
        print('YES')
        continue
    if nech == n or nech == 0:
        print('NO')
    else:
        print('YES')
