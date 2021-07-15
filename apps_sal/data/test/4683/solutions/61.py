import sys
#import time
from collections import deque, Counter, defaultdict
#from fractions import gcd
import bisect
import heapq
#import math
import itertools
import numpy as np
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
inf = 10**18
MOD = 1000000007
ri = lambda : int(input())
rs = lambda : input().strip()
rl = lambda : list(map(int, input().split()))
mod = 998244353

n = ri()
a = rl()
cs = 0
li = []
for i in a:
    cs+=i
    li.append(cs)
sum_ = sum(a)
ans = 0
for i in range(len(a)):
    ans += a[i]*(sum_-li[i])%MOD
print(ans%MOD)
