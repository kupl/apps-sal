import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np
from functools import reduce

rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: sys.stdin.readline().split()
ri = lambda: int(sys.stdin.readline())
rm = lambda: list(map(int, sys.stdin.readline().split()))
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')
mod = 10**9 + 7

n = ri()
a = [ri() for _ in range(n)]
idx = 1
cnt = 1
if a[0] == 2:
    print((1))
    return
while idx != -1:
    a[idx - 1], idx = -1, a[idx - 1]
    cnt += 1
    if a[idx - 1] == 2:
        print(cnt)
        return
print((-1))
