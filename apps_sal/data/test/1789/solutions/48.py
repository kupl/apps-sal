import math
import copy
import bisect
from itertools import accumulate
from collections import Counter, defaultdict, deque
def mp(): return map(int, input().split())
def lmp(): return list(map(int, input().split()))
def ceil(U, V): return (U + V - 1) // V
def modf1(N, MOD): return (N - 1) % MOD + 1


a, b, x, y = mp()
u = x * 2
if a == b:
    print(x)
elif a > b:
    sa = a - b - 1
    print(min(sa * u + x, sa * y + x))
else:
    sa = b - a
    print(min(x + sa * y, sa * u + x))
