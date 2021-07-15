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

a, b, c = rm()
len_ = 1
s = set()
s.add(a)
i = a
while len_ == len(s):
    i += a
    i %= b
    len_ += 1
    s.add(i)
for i in list(s):
    if i == c:
        print('YES')
        return
else:
    print('NO')












