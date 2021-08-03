# Template 1.0
import sys
import re
import math
from collections import deque, defaultdict, Counter, OrderedDict
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from heapq import heappush, heappop, heapify, nlargest, nsmallest
def STR(): return list(input())
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(): return list(map(int, input().split()))
def list2d(a, b, c): return [[c] * b for i in range(a)]
def sortListWithIndex(listOfTuples, idx): return (sorted(listOfTuples, key=lambda x: x[idx]))


def sortDictWithVal(passedDic):
    temp = sorted(list(passedDic.items()), key=lambda kv: (kv[1], kv[0]))
    toret = {}
    for tup in temp:
        toret[tup[0]] = tup[1]
    return toret


def sortDictWithKey(passedDic):
    return dict(OrderedDict(sorted(passedDic.items())))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

t = INT()

while (t != 0):
    n, m = MAP()

    print(n + m)
    t -= 1
