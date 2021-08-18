import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(): return list(map(int, input().split()))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7


def main():
    N, M = MAP()
    S = input()

    pos_0 = []
    for i in range(N + 1):
        if S[i] == "0":
            pos_0.append(i)

    q = deque([])
    pos = N
    while pos != 0:
        next_pos = pos - M
        idx = bisect_left(pos_0, next_pos)
        if pos - pos_0[idx] > M or pos == pos_0[idx]:
            print((-1))
            return

        q.appendleft(pos - pos_0[idx])
        pos = pos_0[idx]

    print((*q))


def __starting_point():
    main()


__starting_point()
