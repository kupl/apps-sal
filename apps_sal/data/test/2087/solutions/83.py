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

a, b, c = rm()
ans = 1
c = (c + 1) * c // 2
ans *= c
ans %= mod2
b = (b + 1) * b // 2
ans *= b
ans %= mod2
a = (a + 1) * a // 2
ans *= a
ans %= mod2
print(ans)
