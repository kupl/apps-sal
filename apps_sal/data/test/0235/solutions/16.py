
import sys
import math
import os.path
import random
from copy import deepcopy
from functools import reduce
from collections import Counter, ChainMap, defaultdict
from itertools import cycle, chain
from queue import Queue, PriorityQueue
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, nlargest, nsmallest
import bisect
from statistics import mean, mode, median, median_low, median_high
# CONFIG
sys.setrecursionlimit(1000000000)
# LOG 
def log(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
# INPUT
def ni():
    return map(int, input().split())
def nio(offset):
    return map(lambda x: int(x) + offset, input().split())
def nia():
    return list(map(int, input().split()))
# CONVERT
def toString(aList, sep=" "):
    return sep.join(str(x) for x in aList)
def toMapInvertIndex(aList):
    return {k: v for v, k in enumerate(aList)}
# SORT
def sortId(arr):
    return sorted(range(arr), key=lambda k: arr[k])
# MATH
def gcd(a,b):
    while b:
        a, b = b, a % b
    return a
# MAIN

n, = ni()

def check(k):
    v = 0
    p = 0
    x = n
    # log("check",k)
    while (x > 0):
        if (x > k):
            v += k
            x -= k
            if (x > 9):
                pd = x // 10
                p += pd
                x -= pd
        else:
            v += x
            x = 0
        
        # log(" ", x, v, p)
    
    # log(k,v,p)
    return v >= p

def bsearch(low, high):
    # log(low,high)
    if (low >= high):
        return low
    mid = (low + high) // 2
    if check(mid):
        return bsearch(low, mid)
    else:
        return bsearch(mid+1, high)


x = bsearch(1,n)
# log(x)
print(x)
