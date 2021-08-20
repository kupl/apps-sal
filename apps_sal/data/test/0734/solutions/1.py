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
za = getIntList()
za.sort(reverse=True)
re = 0
for i in range(N - 1):
    a = za[i]
    b = za[i + 1]
    g = b
    if g >= a:
        t = a - 1
        if t < 1:
            t = 1
        re += g - t
        za[i + 1] = t
        re += a - 1
    else:
        re += g
print(re)
