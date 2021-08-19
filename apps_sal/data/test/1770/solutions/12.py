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
(T,) = getIntList()
for _ in range(T):
    (n, x, y, d) = getIntList()
    y -= 1
    x -= 1
    f = abs(y - x)
    if f % d == 0:
        print(f // d)
        continue
    g1 = (x - 1) // d + 1
    r1 = -1
    if y % d == 0:
        r1 = y // d + g1
    g2 = (n - 1 - x - 1) // d + 1
    r2 = -1
    if (n - 1 - y) % d == 0:
        r2 = (n - 1 - y) // d + g2
    if r1 > 0 and r2 > 0:
        print(min(r1, r2))
        continue
    print(max(r1, r2))
