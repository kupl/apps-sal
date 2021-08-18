from math import ceil, floor, factorial, gcd, sqrt, log2, cos, sin, tan, acos, asin, atan, degrees, radians, pi, inf, comb
from itertools import accumulate, groupby, permutations, combinations, product, combinations_with_replacement
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
from operator import itemgetter
from heapq import heapify, heappop, heappush
from queue import Queue, LifoQueue, PriorityQueue
from copy import deepcopy
from time import time
from functools import reduce
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(MAP())

# レベルnバーガー


def dfs(k):
    nonlocal count, ans
    # バン
    count += 1
    if k == 0:
        ans += 1
    elif count < x:
        # レベルn-1バーガー
        if count + b[k - 1] > x:
            dfs(k - 1)
        else:
            count += b[k - 1]
            ans += p[k - 1]
        if count < x:
            # パティ
            count += 1
            ans += 1
            if count < x:
                # レベルn-1バーガー
                if count + b[k - 1] > x:
                    dfs(k - 1)
                else:
                    count += b[k - 1]
                    ans += p[k - 1]


n, x = MAP()
b = [0] * n
p = [0] * n
b[0] = 1
p[0] = 1
for i in range(1, n):
    b[i] = b[i - 1] * 2 + 3
    p[i] = p[i - 1] * 2 + 1

count = 0
ans = 0
dfs(n)
print(ans)
