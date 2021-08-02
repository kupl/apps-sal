import sys
import numpy as np
from math import ceil as C, floor as F, sqrt
from collections import defaultdict as D, Counter as CNT
from functools import reduce as R
import heapq as H

ALP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alp = 'abcdefghijklmnopqrstuvwxyz'
def _X(): return sys.stdin.readline().rstrip().split(' ')
def _S(ss): return tuple(ss) if len(ss) > 1 else ss[0]
def S(): return _S(_X())
def Ss(): return list(S())
def _I(ss): return tuple([int(s) for s in ss]) if isinstance(ss, tuple) else int(ss)
def I(): return _I(S())
def _Is(ss): return list(ss) if isinstance(ss, tuple) else [ss]
def Is(): return _Is(I())
def rec(h, w): return [[0] * w for i in range(h)]


n = I()
xs = Is()

xs = sorted(xs, reverse=True)

seats = [-xs[0]]
H.heapify(seats)

ans = 0
for x in xs[1:]:
    ans -= H.heappop(seats)
    H.heappush(seats, -x)
    H.heappush(seats, -x)

print(ans)
