from heapq import heapify, heappush, heappop
from collections import Counter, defaultdict, deque, OrderedDict
from sys import setrecursionlimit, maxsize
from bisect import bisect_left, bisect, insort_left, insort
from math import ceil, log, factorial, hypot, pi
from fractions import gcd
from copy import deepcopy
from functools import reduce
from operator import mul
from itertools import product, permutations, combinations, accumulate, cycle
from string import ascii_uppercase, ascii_lowercase, ascii_letters, digits, hexdigits, octdigits


def prod(l):
    return reduce(mul, l)


def prodmod(l, mod):
    return reduce(lambda x, y: mul(x, y) % mod, l)


def read_list(t):
    return [t(x) for x in input().split()]


def read_line(t):
    return t(input())


def read_lines(t, N):
    return [t(input()) for _ in range(N)]


N = read_line(int)
ans = 0
for i in range(len(str(N))):
    ans += N - 10 ** i + 1
print(ans)
