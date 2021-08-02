import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np

rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: sys.stdin.readline().split()
ri = lambda: int(sys.stdin.readline())
rm = lambda: list(map(int, sys.stdin.readline().split()))
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')
mod = 10**9 + 7

n = ri()
a = rl()
c = collections.Counter(a)
ans = 0
if n == 1:
    print((1))
    return
if n == 2:
    if abs(a[0] - a[1]) == 1:
        print((2))
        return
    else:
        print((1))
        return
for i in range(10**5 + 2):
    ans = max(ans, c[i] + c[i + 1] + c[i + 2])
print(ans)
