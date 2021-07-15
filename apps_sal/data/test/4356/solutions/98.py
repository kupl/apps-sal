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
a = [rr() for _ in range(n)]
b = [rr() for _ in range(m)] 
for i in range(n-m+1):
    for j in range(n-m+1):
        c = [s[j:j+m] for s in a[i:i+m]]
        if c == b:
            print('Yes')
            return
print('No')




