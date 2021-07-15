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
mod = 10**9 + 7

d, n = rm()
if n != 100:
    print(((n - (n-1)//99)*100**d))
else:
    print((101 * 100**d))


