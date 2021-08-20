import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop
from functools import reduce, lru_cache


def input():
    return sys.stdin.readline().strip()


def INT():
    return int(input())


def MAP():
    return list(map(int, input().split()))


def LIST():
    return list(map(int, input().split()))


def TUPLE():
    return tuple(map(int, input().split()))


def ZIP(n):
    return list(zip(*(MAP() for _ in range(n))))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7
(n, m) = MAP()
x = LIST()
y = LIST()


def acc(A):
    acc = []
    tmp = 0
    for a in A:
        tmp += a
        tmp %= mod
        acc.append(tmp)
    return acc


def sum_combinations(A, k):
    A_acc = acc(A)
    A_sum = 0
    for i in range(k):
        tmp = (A_acc[-1] - A_acc[i]) % mod
        tmp = (tmp - A[i] * (k - 1 - i) % mod) % mod
        A_sum = (A_sum + tmp) % mod
    return A_sum


print(sum_combinations(x, n) * sum_combinations(y, m) % mod)
