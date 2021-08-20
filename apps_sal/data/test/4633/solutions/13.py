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


mod = int(1000000000.0) + 7
INF = 2 ** 32


def cal(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans


for t in range(int(data())):
    (n, s) = mdata()
    ans = 0
    t = 1
    while cal(n) > s:
        last = n % 10
        n //= 10
        if last != 0:
            ans += t * (10 - last)
            n += 1
        t *= 10
    out(ans)
