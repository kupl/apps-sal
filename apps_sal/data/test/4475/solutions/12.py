import sys, math
import io, os
#data = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
from bisect import bisect_left as bl, bisect_right as br, insort
from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
# from itertools import permutations,combinations
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var): sys.stdout.write('\n'.join(map(str, var)) + '\n')
def out(var): sys.stdout.write(str(var) + '\n')
from decimal import Decimal
# from fractions import Fraction
# sys.setrecursionlimit(100000)
mod = int(1e9) + 7
INF=2**32

for t in range(int(data())):
    a,b,x,y,n=mdata()
    m1=max(a-n,x)
    m2=max(b-n,y)
    if m1<m2:
        m2=max(b-(n-(a-m1)),y)
    else:
        m1=max(a-(n-(b-m2)),x)
    out(m1*m2)
