import sys
from collections import deque, Counter, defaultdict
import bisect
import heapq
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

n = ri()
a = rl()
cs = 0
li = []
for i in a:
    cs += i
    li.append(cs)
sum_ = sum(a)
ans = 0
for i in range(len(a)):
    ans += a[i] * (sum_ - li[i]) % MOD
print(ans % MOD)
