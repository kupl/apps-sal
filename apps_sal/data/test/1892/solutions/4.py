import sys
import time
import re
import string
import math
from operator import itemgetter
from collections import Counter
from collections import deque
from collections import defaultdict as dd
import fractions
from heapq import heappop, heappush, heapify
import array
from bisect import bisect_left, bisect_right, insort_left, insort_right
from copy import deepcopy as dcopy
import itertools
sys.setrecursionlimit(10**7)
inf = 10**20
gosa = 1.0 / 10**10
mod = 10**9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


N = int(input())


def solve():
    A = []
    for n in range(N):
        A.append(input())

    dp = [[0] * (N + 1) for n in range(N + 1)]
    dp[0][0] = 1
    pre_a = A[0]
    for i, a in enumerate(A):
        if i == 0:
            continue
        if pre_a == 'f':
            for j in reversed(list(range(i + 1))):
                dp[i][j] = dp[i - 1][j - 1]
        else:
            s = 0
            for j in reversed(list(range(i))):
                s += dp[i - 1][j]
                s %= mod
                dp[i][j] = s

        pre_a = a

    res = 0
    for v in dp[N - 1]:
        res += v
        res = res % mod
    print(res)


def __starting_point():
    solve()


__starting_point()
