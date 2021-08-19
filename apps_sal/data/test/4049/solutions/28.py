import sys
import math
from collections import Counter, deque, defaultdict
from bisect import bisect_left, bisect_right
mod = 10 ** 9 + 7
INF = float('inf')


def inp():
    return int(sys.stdin.readline())


def inpl():
    return list(map(int, sys.stdin.readline().split()))


n = inp()
a = inpl()
b = inpl()
sua = sum(a)
sub = sum(b)
mi_res = 0
if a[0] > b[0] + b[2]:
    mi_res = a[0] - b[0] - b[2]
if a[1] > b[0] + b[1]:
    mi_res = a[1] - b[0] - b[1]
if a[2] > b[2] + b[1]:
    mi_res = a[2] - b[2] - b[1]
ma_res = min(a[0], b[1]) + min(a[1], b[2]) + min(a[2], b[0])
print(mi_res, ma_res)
