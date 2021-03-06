from fractions import Fraction
import sys
import math
import io
import os
from bisect import bisect_left as bl, bisect_right as br, insort
from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter


def data():
    return sys.stdin.readline().strip()


def mdata():
    return list(map(int, data().split()))


def outl(var):
    sys.stdout.write('\n'.join(map(str, var)) + '\n')


def out(var):
    sys.stdout.write(str(var) + '\n')


INF = float('inf')
mod = int(1000000000.0) + 7
for t in range(int(data())):
    (n, k, l) = mdata()
    d = mdata()
    flag = True
    m = k
    p = 0
    for j in range(0, n):
        if l - d[j] >= k:
            m = k - 1
            p = 0
        else:
            if d[j] + m > l and p == 1 or d[j] > l:
                flag = False
                break
            if p == 0:
                m = min(m - 1, l - d[j] - 1)
                if m == -1:
                    p = 1
                    m = 1
            else:
                m += 1
    if flag == True:
        out('Yes')
    else:
        out('No')
