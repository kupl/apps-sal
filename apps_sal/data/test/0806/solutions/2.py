import collections
import atexit
import math
import sys
import bisect
sys.setrecursionlimit(1000000)


def getIntList():
    return list(map(int, input().split()))


try:
    import numpy

    def dprint(*args, **kwargs):
        print(*args, file=sys.stderr)
    dprint('debug mode')
except Exception:

    def dprint(*args, **kwargs):
        pass
inId = 0
outId = 0
if inId > 0:
    dprint('use input', inId)
    sys.stdin = open('input' + str(inId) + '.txt', 'r')
if outId > 0:
    dprint('use output', outId)
    sys.stdout = open('stdout' + str(outId) + '.txt', 'w')
    atexit.register(lambda: sys.stdout.close())
(N, L, R) = getIntList()
base = 10 ** 9 + 7
g = R - L + 1
f = g // 3
zz = [f, f, f]
for i in range(g % 3):
    t = (i + L) % 3
    zz[t] += 1
dp = zz.copy()
dprint(dp)
for _ in range(1, N):
    dp1 = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            dp1[(i + j) % 3] += dp[i] * zz[j]
    for i in range(3):
        dp1[i] %= base
    dp = dp1
    dprint(dp)
print(dp[0])
