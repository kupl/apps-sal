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

s = rr()
t = rr()
for i in range(len(s)+3):
    if s == t:
        print('Yes')
        return
    else:
        s = s[-1] + s[:-1]
print('No')
        











