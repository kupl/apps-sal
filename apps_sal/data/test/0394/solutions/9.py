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

N, = getIntList()
za = [0, ] + getIntList()
zb = []
for i in range(N):
    zb.append(za[i + 1] - za[i])

dprint(zb)

res = [N]
for i in range(1, N):
    ok = True
    for j in range(i, N):
        if zb[j] != zb[j % i]:
            ok = False
            break
    if ok:
        res.append(i)

res.sort()
print(len(res))
for x in res:
    print(x, end=' ')
