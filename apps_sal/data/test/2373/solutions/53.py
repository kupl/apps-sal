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


def INPUT():
    return sys.stdin.readline().rstrip()


def INT():
    return int(INPUT())


def MAP():
    return list(map(int, INPUT().split()))


def S_MAP():
    return list(map(str, INPUT().split()))


def LIST():
    return list(map(int, INPUT().split()))


def S_LIST():
    return list(map(str, INPUT().split()))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7


def main():
    N = INT()
    P = LIST()
    P.append(-1)
    cnt = 0
    i = 0
    while i < N:
        if P[i] == i + 1:
            cnt += 1
            i += P[i + 1] == i + 2
        i += 1
    print(cnt)


def __starting_point():
    main()


__starting_point()
