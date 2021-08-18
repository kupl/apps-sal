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

s = rr()
t = rr()
for i in range(len(s) + 3):
    if s == t:
        print('Yes')
        return
    else:
        s = s[-1] + s[:-1]
print('No')
