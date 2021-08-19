from decimal import Decimal
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


mod = int(1000000000.0) + 7
INF = 2 ** 32
for t in range(int(data())):
    (a, b, x, y, n) = mdata()
    m1 = max(a - n, x)
    m2 = max(b - n, y)
    if m1 < m2:
        m2 = max(b - (n - (a - m1)), y)
    else:
        m1 = max(a - (n - (b - m2)), x)
    out(m1 * m2)
