from decimal import Decimal
import sys
import math
import io
import os
#data = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
#from bisect import bisect_left as bl, bisect_right as br, insort
#from heapq import heapify, heappush, heappop
#from collections import defaultdict as dd, deque, Counter
#from itertools import permutations,combinations
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var): sys.stdout.write(' '.join(map(str, var)) + '\n')
def out(var): sys.stdout.write(str(var) + '\n')


#from fractions import Fraction
# sys.setrecursionlimit(100000)
INF = float('inf')
mod = int(1e9) + 7

for t in range(int(data())):
    n = int(data())
    a = mdata()
    a1 = sorted(a)
    k = 1
    for i in range(n):
        if a[i] != a1[i] and a[i] % a1[0] != 0:
            k = 0
            break
    if k:
        out("YES")
    else:
        out("NO")
