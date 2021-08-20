import sys
import math
import os
from io import BytesIO, IOBase
from collections import defaultdict as dd, deque, Counter


def data():
    return sys.stdin.readline().strip()


def mdata():
    return list(map(int, data().split()))


def outl(var):
    sys.stdout.write(' '.join(map(str, var)) + '\n')


def out(var):
    sys.stdout.write(str(var) + '\n')


INF = 10 ** 9
mod = 998244353
for t in range(int(data())):
    (n, k) = mdata()
    a = mdata()
    d = dd(int)
    for i in range(n):
        if a[i] % k == 0:
            continue
        d[k - a[i] % k] += 1
    m = 0
    for i in d:
        m = max(m, i + k * (d[i] - 1))
    if m == 0:
        out(0)
    else:
        out(m + 1)
