from math import ceil, floor, factorial, gcd, sqrt, log2, cos, sin, tan, acos, asin, atan, degrees, radians, pi, inf
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


#i - j == a[i] + a[j]
# => i - a[i] == j + a[j]
#j - i == a[i] + a[j]
# => i + a[i] == j - a[j]
n = INT()
a = LIST()
c = [0] * (2 * n + 1)
for i in range(n):
    if i - a[i] >= 0:
        c[i - a[i]] += 1
ans = 0
for i in range(n):
    if i + a[i] <= 2 * n:
        ans += c[i + a[i]]
print(ans)
