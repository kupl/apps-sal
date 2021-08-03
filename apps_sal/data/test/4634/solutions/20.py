import sys
import math
import itertools
from collections import Counter, deque, defaultdict
from bisect import bisect_left, bisect_right
mod = 10**9 + 7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))


for _ in range(inp()):
    n = inp()
    a = inpl()
    st = la = 0
    for i in range(n):
        if a[i]:
            st = i
            break
    for i in range(n)[::-1]:
        if a[i]:
            la = i
            break

    ch = False
    res = 0
    for i in range(st, la + 1):
        x = a[i]
        if ch:
            if x:
                continue
            ch = False
            res += 1
        else:
            if x:
                ch = True
            else:
                res += 1
    print(res)
