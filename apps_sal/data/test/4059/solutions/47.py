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
ans = 0
for a in range(1, n):
    ans += (n-1)//a
print(ans)


