import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np
from functools import reduce


def rr(): return sys.stdin.readline().rstrip()
def rs(): return sys.stdin.readline().split()
def ri(): return int(sys.stdin.readline())
def rm(): return list(map(int, sys.stdin.readline().split()))
def rl(): return list(map(int, sys.stdin.readline().split()))


inf = float('inf')
mod = 10**9 + 7


n, m = rm()
a = [rr() for _ in range(n)]
b = [rr() for _ in range(m)]
for i in range(n - m + 1):
    for j in range(n - m + 1):
        c = [s[j:j + m] for s in a[i:i + m]]
        if c == b:
            print('Yes')
            return
print('No')
