import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque, Counter
from decimal import Decimal


def s():
    return input()


def i():
    return int(input())


def S():
    return input().split()


def I():
    return map(int, input().split())


def L():
    return list(map(int, input().split()))


def l():
    return list(map(int, input().split()))


def lcm(a, b):
    return a * b // math.gcd(a, b)


sys.setrecursionlimit(10 ** 9)
INF = 10 ** 9
mod = 10 ** 9 + 7
(N, A, B, C) = I()
l = [i() for _ in range(N)]


def dfs(cur, a, b, c):
    if cur == N:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else INF
    ret0 = dfs(cur + 1, a, b, c)
    ret1 = dfs(cur + 1, a + l[cur], b, c) + 10
    ret2 = dfs(cur + 1, a, b + l[cur], c) + 10
    ret3 = dfs(cur + 1, a, b, c + l[cur]) + 10
    return min(ret0, ret1, ret2, ret3)


print(dfs(0, 0, 0, 0))
