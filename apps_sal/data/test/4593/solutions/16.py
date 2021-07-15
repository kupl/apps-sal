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

x = ri()
max_ = 0
for i in range(int(x**0.5), 0, -1):
    for j in range(1, 10):
        if i**j <= x:
            max_ = max(i**j, max_)
        else:
            break
print(max_)











