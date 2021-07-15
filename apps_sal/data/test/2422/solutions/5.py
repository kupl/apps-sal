import sys, math
import io, os
#data = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
from bisect import bisect_left as bl, bisect_right as br, insort
from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
#from itertools import permutations,combinations
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var) : sys.stdout.write('\n'.join(map(str, var))+'\n')
def out(var) : sys.stdout.write(str(var)+'\n')
#from decimal import Decimal
#from fractions import Fraction
#sys.setrecursionlimit(100000)
INF = float('inf')
mod=10**9+7


for t in range(int(data())):
    n=int(data())
    k=n//3
    if n%3==2:
        if k<1:
            print(-1)
            continue
        print(k-1,1,0)
    elif n%3==1:
        if k<2:
            print(-1)
            continue
        print(k-2,0,1)
    else:
        print(k,0,0)
