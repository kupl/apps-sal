from math import floor, ceil, pi, factorial
from bisect import bisect_left, bisect_right
from copy import deepcopy
from operator import itemgetter
from heapq import heapify, heappop, heappush
from itertools import combinations, permutations, accumulate, groupby, product
from collections import defaultdict
from collections import Counter, deque
import sys
import numpy
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def I():
    return int(input())


def MI():
    return map(int, input().split())


def LI():
    return list(map(int, input().split()))


def LI2():
    return [int(input()) for i in range(n)]


def MXI():
    return [[LI()] for i in range(n)]


def SI():
    return input().rstrip()


def printns(x):
    print('\n'.join(x))


def printni(x):
    print('\n'.join(list(map(str, x))))


inf = 10 ** 17
mod = 10 ** 9 + 7
(h, w) = MI()
if w % 3 == 0:
    s1 = 0
else:
    s1 = h
if h % 3 == 0:
    s2 = 0
else:
    s2 = w
fw = floor(w / 3)
fh = floor(h / 2)
cw = ceil(w / 3)
SMAX1 = (w - fw) * (h - fh)
SMIN1 = min(fw * h, (w - fw) * fh)
SMAX2 = max(cw * h, (w - cw) * (h - fh))
SMIN2 = (w - cw) * fh
s3 = min(SMAX1 - SMIN1, SMAX2 - SMIN2)
(h, w) = (w, h)
fw = floor(w / 3)
fh = floor(h / 2)
cw = ceil(w / 3)
SMAX1 = (w - fw) * (h - fh)
SMIN1 = min(fw * h, (w - fw) * fh)
SMAX2 = max(cw * h, (w - cw) * (h - fh))
SMIN2 = (w - cw) * fh
s4 = min(SMAX1 - SMIN1, SMAX2 - SMIN2)
ans = min(s1, s2, s3, s4)
print(ans)
