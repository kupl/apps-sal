import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys


def input():
    return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10 ** 7)
INF = float('inf')
MOD = 10 ** 9 + 7


def I():
    return int(input())


def F():
    return float(input())


def SS():
    return input()


def LI():
    return [int(x) for x in input().split()]


def LI_():
    return [int(x) - 1 for x in input().split()]


def LF():
    return [float(x) for x in input().split()]


def LSS():
    return input().split()


def primeFactorization(n):
    ans = []
    temp = n
    while temp % 2 == 0:
        ans.append(2)
        temp //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while temp % i == 0:
            ans.append(i)
            temp //= i
    if temp > 1:
        ans.append(temp)
    return collections.Counter(ans)


def combMod(n, r, p):
    numer = 1
    denom = 1
    for i in range(1, r + 1):
        numer = numer * (n - r + i) % p
        denom = denom * i % p
    return numer * pow(denom, p - 2, p) % p


def resolve():
    (N, M) = LI()
    pf = primeFactorization(M)
    ans = 1
    for i in list(pf.values()):
        ans *= combMod(i + N - 1, i, MOD)
        ans %= MOD
    print(ans)


def __starting_point():
    resolve()


__starting_point()
