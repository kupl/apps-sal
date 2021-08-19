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


def isin(x, y, M):
    if M[0] <= x <= M[2] and M[1] <= y <= M[3]:
        return True
    return False


for _ in range(T):
    (N, M) = getIntList()
    m1 = getIntList()
    m2 = getIntList()
    zx = [0, M]
    zx += [m1[0] - 1, m1[2]]
    zx += [m2[0] - 1, m2[2]]
    zx.sort()
    zy = [0, N]
    zy += [m1[1] - 1, m1[3]]
    zy += [m2[1] - 1, m2[3]]
    zy.sort()
    totB = 0
    for i0 in range(5):
        if zx[i0] == zx[i0 + 1]:
            continue
        for i1 in range(5):
            if zy[i1] == zy[i1 + 1]:
                continue
            x0 = zx[i0] + 1
            y0 = zy[i1] + 1
            dprint('x0,y0', x0, y0)
            size = (zx[i0 + 1] - zx[i0]) * (zy[i1 + 1] - zy[i1])
            if isin(x0, y0, m2):
                dprint('black')
                totB += size
            elif isin(x0, y0, m1):
                dprint('white')
                pass
            else:
                totB += size // 2
                if size % 2 == 1:
                    if (x0 + y0) % 2 == 1:
                        dprint('extra black')
                        totB += 1
    print(N * M - totB, totB)
