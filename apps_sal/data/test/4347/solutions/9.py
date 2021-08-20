from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush, heappop
import math
from collections import *
from functools import reduce, cmp_to_key, lru_cache
import sys
input = sys.stdin.readline
M = mod = 998244353


def factors(n):
    return sorted(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))))


def inv_mod(n):
    return pow(n, mod - 2, mod)


def li():
    return [int(i) for i in input().rstrip('\n').split()]


def st():
    return input().rstrip('\n')


def val():
    return int(input().rstrip('\n'))


def li2():
    return [i for i in input().rstrip('\n')]


def li3():
    return [int(i) for i in input().rstrip('\n')]


@lru_cache(None)
def fact(n):
    ans = 1
    if n == 0:
        return 1
    for i in range(1, n + 1):
        ans *= i
    return ans


def ncr(n, r):
    return fact(n) / (fact(r) * fact(n - r))


n = val()
print(int(ncr(n, n // 2) * fact(n // 2 - 1) ** 2 // 2))
