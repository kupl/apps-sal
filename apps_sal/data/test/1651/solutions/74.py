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
def rf(): return list(map(float, sys.stdin.readline().split()))
def rl(): return list(map(int, sys.stdin.readline().split()))


inf = float('inf')
mod1 = 10**9 + 7
mod2 = 998244353
al = 'abcdefghijklmnopqrstuvwxyz'
Al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

s, p = rm()
for i in range(1, 10**6 + 1):
    if p % i == 0 and i + p // i == s:
        print('Yes')
        return
print('No')
