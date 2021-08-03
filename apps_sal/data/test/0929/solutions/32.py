from math import ceil, floor, factorial, gcd, sqrt, log2, cos, sin, tan, acos, asin, atan, degrees, radians, pi, inf, comb
from itertools import accumulate, groupby, permutations, combinations, product, combinations_with_replacement
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
from operator import itemgetter
from heapq import heapify, heappop, heappush
from queue import Queue, LifoQueue, PriorityQueue
from copy import deepcopy
from time import time
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(MAP())


h, w = MAP()
a = [[0] * (w + 1)]
for i in range(1, h + 1):
    a.append([0] + LIST())
ans = []
flag = False
for i in range(1, h + 1):
    if i % 2 == 1:
        for j in range(1, w + 1):
            if a[i][j] % 2 == 1:
                flag = not flag
            if flag:
                if j < w:
                    ans.append([i, j, i, j + 1])
                elif i < h:
                    ans.append([i, j, i + 1, j])
    else:
        for j in range(w, 0, -1):
            if a[i][j] % 2 == 1:
                flag = not flag
            if flag:
                if j > 1:
                    ans.append([i, j, i, j - 1])
                elif i < h:
                    ans.append([i, j, i + 1, j])

print(len(ans))
for x in ans:
    print(*x)
