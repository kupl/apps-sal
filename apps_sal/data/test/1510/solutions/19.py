import os
import sys
import bisect
import copy
from collections import defaultdict, Counter, deque
from functools import lru_cache
if os.path.exists('in.txt'):
    sys.stdin = open('in.txt', 'r')
if os.path.exists('out.txt'):
    sys.stdout = open('out.txt', 'w')


def input():
    return sys.stdin.readline()


def mapi(arg=0):
    return list(map(int if arg == 0 else str, input().split()))


(n, m) = mapi()
a = list(mapi())
b = list(mapi())
a.sort()
b.sort(reverse=True)
res = 0
i = 0
while i < n and i < m and (a[i] < b[i]):
    res += b[i] - a[i]
    i += 1
print(res)
