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
    N, H = MAP()
    A, B = [0] * N, [0] * N
    for i in range(N):
        A[i], B[i] = MAP()

    MAX_A = max(A)
    B.sort(reverse=True)

    ans = 0
    for i in range(N):
        if MAX_A >= B[i]:
            ans += -(-H // MAX_A)
            print(ans)
            break
        else:
            H -= B[i]
            ans += 1

        if H <= 0:
            print(ans)
            break
    else:
        ans += -(-H // MAX_A)
        print(ans)


def __starting_point():
    main()


__starting_point()
