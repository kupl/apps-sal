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
    sys.stdout.write(' '.join(map(str, var)) + '\n')


def out(var):
    sys.stdout.write(str(var) + '\n')


mod = 998244353
INF = float('inf')
for t in range(int(data())):
    n = int(data())
    a = data()
    if n % 2 == 0:
        k = 0
        for i in range(1, n, 2):
            if int(a[i]) % 2 == 0:
                k = 1
        if k:
            out(2)
        else:
            out(1)
    else:
        k = 0
        for i in range(0, n, 2):
            if int(a[i]) % 2 == 1:
                k = 1
        if k:
            out(1)
        else:
            out(2)
