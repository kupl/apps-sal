import sys
import math
from collections import Counter, deque, defaultdict
from bisect import bisect_left, bisect_right
mod = 10**9 + 7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))


n = inp()
a = inpl()
res = 0
now = 0
se = set()
for x in a:
    now += x
    if now in se or now == 0:
        res += 1
        now = x
        se = set()
        se.add(now)
    else:
        se.add(now)
print(res)
