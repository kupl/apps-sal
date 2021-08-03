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

n = ri()
cnt = 0
for v in list(collections.Counter([ri() for _ in range(n)]).values()):
    if v & 1:
        cnt += 1
print(cnt)
