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

n, m = rm()
li = [[] for _ in range(n)]
for _ in range(m):
    a, b = rm()
    a -= 1
    b -= 1
    li[a].append(b)
    li[b].append(a)
for lis in li:
    print((len(lis)))














