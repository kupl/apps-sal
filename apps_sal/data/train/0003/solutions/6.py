import sys
import math
import io
import os
from bisect import bisect_left as bl, bisect_right as br, insort
from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var): sys.stdout.write('\n'.join(map(str, var)) + '\n')
def out(var): sys.stdout.write(str(var) + '\n')


INF = float('inf')
mod = 10**9 + 7


for t in range(int(data())):
    n, k = mdata()
    a = sorted(mdata(), reverse=True)
    s = sum(a[:k + 1])
    out(s)
