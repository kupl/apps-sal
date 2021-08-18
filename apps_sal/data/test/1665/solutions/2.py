from bisect import bisect_left as bl, bisect_right as br, insort
import sys
import heapq
from math import *
from collections import defaultdict as dd, deque
def data(): return sys.stdin.readline().strip()
def mdata(): return map(int, data().split())


n = int(input())
t = [dd(int) for i in range(n)]
l = []
for i in range(n - 1):
    u, v = mdata()
    t[u - 1][v - 1] = 0
    t[v - 1][u - 1] = 0
    l.append([u - 1, v - 1])
s = 0
e = n - 2
for i in range(n - 1):
    a, b = l[i]
    if len(t[a]) == 1 or len(t[b]) == 1:
        print(s)
        s += 1
    else:
        print(e)
        e -= 1
