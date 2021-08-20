import sys
import math
import os.path
from copy import deepcopy
from functools import reduce
from pprint import pprint
from collections import Counter, ChainMap, defaultdict
from itertools import cycle, chain
from queue import Queue, PriorityQueue, deque
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, nlargest, nsmallest
import bisect
from statistics import mean, mode, median, median_low, median_high
sys.setrecursionlimit(10 ** 9)


def log(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def ni():
    return list(map(int, input().split()))


def nio(offset):
    return [int(x) + offset for x in input().split()]


def nia():
    return list(map(int, input().split()))


def toString(aList, sep=' '):
    return sep.join((str(x) for x in aList))


def toMapInvertIndex(aList):
    return {k: v for (v, k) in enumerate(aList)}


def sortId(arr):
    return sorted(list(range(len(arr))), key=lambda k: arr[k])


(n, m) = ni()
s = [0] * n
for i in range(n):
    ss = input()
    s[i] = ss
dd = [['.' for j in range(m)] for i in range(n)]
res = deque()
for i in range(n):
    for j in range(m):
        if s[i][j] == '*':
            k = 1
            while 0 <= i - k < n and 0 <= i + k < n and (0 <= j - k < m) and (0 <= j + k < m) and (s[i - k][j] == '*') and (s[i + k][j] == '*') and (s[i][j - k] == '*') and (s[i][j + k] == '*'):
                dd[i - k][j] = '*'
                dd[i + k][j] = '*'
                dd[i][j - k] = '*'
                dd[i][j + k] = '*'
                if k == 1:
                    dd[i][j] = '*'
                    res.append((i + 1, j + 1, k))
                else:
                    res[-1] = (i + 1, j + 1, k)
                k += 1


def check():
    for i in range(n):
        for j in range(m):
            if s[i][j] != dd[i][j]:
                return False
    return True


if check():
    lres = len(res)
    print(lres)
    if lres > 0:
        print('\n'.join((' '.join((str(y) for y in x)) for x in res)))
else:
    print(-1)
