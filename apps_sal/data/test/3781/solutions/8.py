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
    n = int(data())
    a = mdata()
    if n % 2 == 1:
        out('Second')
    else:
        a.sort()
        k = 1
        for i in range(n // 2):
            if a[2 * i] != a[2 * i + 1]:
                out('First')
                k = 0
                break
        if k:
            out('Second')
