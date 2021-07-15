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
rf = lambda: list(map(float, sys.stdin.readline().split()))
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')
mod1 = 10**9 + 7
mod2 = 998244353
al = 'abcdefghijklmnopqrstuvwxyz'
Al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

s, p = rm()
for i in range(1, 10**6+1):
    if p%i == 0 and i + p//i == s:
        print('Yes')
        return
print('No')

