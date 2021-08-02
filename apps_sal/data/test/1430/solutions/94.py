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
count = 0
flag = 1
que = deque([0] * (2 * k + 1))
ans = 0
tmp = 0
for x in s:
    if x == '0':
        if flag == 1:
            que.append(count)
            tmp += count - que.popleft()
            ans = max(ans, tmp)
            count = 0
        flag = 0
        count += 1
    else:
        if flag == 0:
            que.append(count)
            tmp += count - que.popleft()
            count = 0
        flag = 1
        count += 1

que.append(count)
tmp += count - que.popleft()
if s[-1] == '0':
    tmp -= que.popleft()
ans = max(ans, sum(que))
print(ans)
