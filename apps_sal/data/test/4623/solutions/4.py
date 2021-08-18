from decimal import Decimal
from fractions import Fraction
import sys
import math
import io
import os
from bisect import bisect_left as bl, bisect_right as br, insort
from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var): sys.stdout.write(' '.join(map(str, var)) + '\n')
def out(var): sys.stdout.write(str(var) + '\n')


INF = float('inf')
mod = int(1e9) + 7

for t in range(int(data())):
    n = int(data())
    w = sorted(mdata())
    ans = 0
    for i in range(2, 2 * max(w) + 1):
        cnt = 0
        s, e = 0, n - 1
        while s < e:
            if w[s] + w[e] == i:
                cnt += 1
                s += 1
                e -= 1
            elif w[s] + w[e] < i:
                s += 1
            else:
                e -= 1
        ans = max(ans, cnt)
    out(ans)
