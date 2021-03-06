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
(N, M) = getIntList()
zs = [N // M for _ in range(M)]
for i in range(1, N % M + 1):
    zs[i] += 1
dprint(zs)
zs1 = [0 for _ in range(M)]
for i in range(M):
    t = i * i % M
    zs1[t] += zs[i]
dprint(zs1)
re = 0
for i in range(1, M):
    re += zs1[i] * zs1[M - i]
re += zs1[0] * zs1[0]
print(re)
