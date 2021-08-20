import sys
import numpy as np
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
mod = 10 ** 9 + 7
INF = 10 ** 18
eps = 10 ** (-7)
(n, k) = map(int, input().split())
a = np.array(readline().split(), np.int64)
f = np.array(readline().split(), np.int64)
a.sort()
f.sort()
f = f[::-1]


def test(x):
    return np.maximum(0, a - x // f).sum() <= k


l = -1
r = INF
while l + 1 < r:
    mid = (l + r) // 2
    if test(mid):
        r = mid
    else:
        l = mid
print(r)
