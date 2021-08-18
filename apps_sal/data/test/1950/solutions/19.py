import os
import sys
import bisect
import copy
from heapq import heappush as pus, heappop as pp, heapify
from collections import defaultdict, Counter, deque
from functools import lru_cache
if os.path.exists('in.txt'):
    sys.stdin = open('in.txt', 'r')
if os.path.exists('out.txt'):
    sys.stdout = open('out.txt', 'w')


def input(): return sys.stdin.readline()
def mapi(arg=0): return list(map(int if arg == 0 else str, input().split()))


n = int(input())
a = list(mapi())
a.sort()
heapify(a)
res = 0
if n % 2 == 0:
    pus(a, 0)
while len(a) > 1:
    if len(a) >= 3:
        tmp = pp(a) + pp(a) + pp(a)
        res += tmp
        pus(a, tmp)
    elif len(a) == 2:
        tmp = pp(a) + pp(a)
        res += tmp
        pus(a, tmp)
print(res)
