import sys
import re
import os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from functools import reduce
from bisect import bisect_left, insort_left
from heapq import heapify, heappush, heappop


def INPUT(): return sys.stdin.readline().rstrip()
def INT(): return int(INPUT())
def MAP(): return list(map(int, INPUT().split()))
def S_MAP(): return list(map(str, INPUT().split()))
def LIST(): return list(map(int, INPUT().split()))
def S_LIST(): return list(map(str, INPUT().split()))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7


def main():
    N = INT()
    A = LIST()

    neg = 0
    m = INF
    for i in range(N):
        if A[i] < 0:
            neg += 1
            A[i] = - A[i]
        m = min(m, A[i])

    if 0 in A:
        print((sum(A)))
    else:
        print((sum(A) - (2 * m) * (neg % 2)))


def __starting_point():
    main()


__starting_point()
