from math import ceil, floor, factorial, gcd, sqrt, log2, cos, sin, tan, acos, asin, atan, degrees, radians, pi, inf
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


n, k = MAP()
s = input()
l = s.count('L')

count = 0
for i in range(n):
    if i > 0 and s[i] == s[i - 1] == 'L':
        count += 1
    elif i < n - 1 and s[i] == s[i + 1] == 'R':
        count += 1

ans = min(count + k * 2, n - 1)
print(ans)
