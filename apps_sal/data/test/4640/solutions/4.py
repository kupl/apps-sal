from decimal import Decimal
import sys
import math
import io
import os
#data = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
from bisect import bisect_left as bl, bisect_right as br, insort
from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
# from itertools import permutations,combinations
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var): sys.stdout.write(' '.join(map(str, var)) + '\n')
def out(var): sys.stdout.write(str(var) + '\n')


# from fractions import Fraction
# sys.setrecursionlimit(100000)
mod = int(1e9) + 7
INF = 2**32


def cal(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans


for t in range(int(data())):
    n, k = mdata()
    ans = 1
    X = sorted(mdata())
    Y = mdata()
    q = deque()
    d = dd(int)
    m = 0
    for i in range(n):
        while q and X[i] - k > q[0]:
            m = max(m, d[q.popleft()])
        q.append(X[i])
        d[X[i]] = len(q)
        ans = max(ans, m + len(q))
    out(ans)
