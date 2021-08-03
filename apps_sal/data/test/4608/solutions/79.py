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
a = [ri() for _ in range(n)]
idx = 1
cnt = 1
if a[0] == 2:
    print((1))
    return
while idx != -1:
    a[idx - 1], idx = -1, a[idx - 1]
    cnt += 1
    if a[idx - 1] == 2:
        print(cnt)
        return
print((-1))
