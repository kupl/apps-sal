from math import floor, ceil, sqrt, factorial, log
from collections import Counter, deque
from functools import reduce
import numpy as np
def S(): return input()
def I(): return int(input())
def MS(): return map(str, input().split())
def MI(): return map(int, input().split())
def LS(): return list(MS())
def LI(): return list(MI())
def LLS(): return [list(map(str, l.split())) for l in input()]
def LLI(): return [list(map(int, l.split())) for l in input()]
def LLSN(n: int): return [LS() for _ in range(n)]
def LLIN(n: int): return [LI() for _ in range(n)]


n, k = MI()

a = np.array(sorted([int(i) for i in input().split()]))

pos = a[a > 0]
zero = a[a == 0]
neg = a[a < 0]

# 2分探索, mid より小さいものを数える
l = -10 ** 18 - 1
r = 10 ** 18 + 1
while r - l > 1:
    mid = (r + l) // 2
    cnt = 0
    if mid >= 0:
        cnt += len(zero) * n

    cnt += a.searchsorted(mid // pos, side="right").sum()
    cnt += (n - a.searchsorted(-(-mid // neg), side="left")).sum()
    cnt -= np.count_nonzero(a * a <= mid)
    cnt //= 2
    if cnt >= k:
        r = mid
    else:
        l = mid

print(r)
