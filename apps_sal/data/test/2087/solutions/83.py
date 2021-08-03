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
