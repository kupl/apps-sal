import sys
from collections import deque, Counter, defaultdict
import bisect
import heapq
import math
import itertools
import numpy as np
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
inf = 10**18
MOD = 1000000007
def ri(): return int(input())
def rs(): return input().strip()
def rl(): return list(map(int, input().split()))


mod = 998244353

a, b, n = rl()
if n / b >= 1:
    print(math.floor(a * (b - 1) / b))
else:
    print(math.floor(a * n / b))
