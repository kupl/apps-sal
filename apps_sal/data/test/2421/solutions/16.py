import sys
import math
import io
import os
#data = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
from bisect import bisect_left as bl, bisect_right as br, insort
from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
#from itertools import permutations,combinations
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var): sys.stdout.write('\n'.join(map(str, var)) + '\n')
def out(var): sys.stdout.write(str(var) + '\n')


#from decimal import Decimal
#from fractions import Fraction
# sys.setrecursionlimit(100000)
INF = float('inf')
mod = 10**9 + 7


for t in range(int(data())):
    y, x = mdata()
    c = mdata()
    if x >= 0 and y >= 0:
        out(min(c[1] * x + c[5] * y, c[0] * min(x, y) + c[1] * (x - min(x, y)) + c[5] * (y - min(x, y)), c[0] * max(x, y) + c[4] * (max(x, y) - x) + c[2] * (max(x, y) - y)))
    elif x > 0 and y < 0:
        y = abs(y)
        out(min(c[1] * x + c[2] * y, c[0] * x + c[2] * (x + y), c[3] * y + c[1] * (x + y)))
    elif x < 0 and y > 0:
        x = abs(x)
        out(min(c[4] * x + c[5] * y, c[3] * x + c[5] * (x + y), c[0] * y + c[4] * (x + y)))
    else:
        x = abs(x)
        y = abs(y)
        out(min(c[4] * x + c[2] * y, c[3] * min(x, y) + c[4] * (x - min(x, y)) + c[2] * (y - min(x, y)),
                c[3] * max(x, y) + c[1] * (max(x, y) - x) + c[5] * (max(x, y) - y)))
