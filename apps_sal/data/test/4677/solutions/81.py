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
ans = ''
for i in s:
    if i == '0':
        ans += '0'
    elif i == '1':
        ans += '1'
    elif ans:
        ans = ans[:-1]
print(ans)
