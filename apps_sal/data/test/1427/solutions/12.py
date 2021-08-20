import sys
import bisect
import math
import itertools
import string
import queue
import copy
import numpy as np
import scipy
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations
from heapq import heappop, heappush
from fractions import gcd
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
mod = 10 ** 9 + 7


def inp():
    return int(input())


def inpm():
    return list(map(int, input().split()))


def inpl():
    return list(map(int, input().split()))


def inpls():
    return list(input().split())


def inplm(n):
    return list((int(input()) for _ in range(n)))


def inplL(n):
    return [list(input()) for _ in range(n)]


def inplT(n):
    return [tuple(input()) for _ in range(n)]


def inpll(n):
    return [list(map(int, input().split())) for _ in range(n)]


def inplls(n):
    return sorted([list(map(int, input().split())) for _ in range(n)])


n = inp()
A = inpl()


def lcm(A):
    from fractions import gcd
    x = A[0]
    for a in A:
        x = x * a // math.gcd(x, a)
    return x


l = lcm(A)
ans = 0
for a in A:
    ans += l // a
print(ans % mod)
