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


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


(la, ra, ta) = getIntList()
(lb, rb, tb) = getIntList()
g = gcd(ta, tb)
wa = ra - la + 1
wb = rb - lb + 1
d = la - lb
d1 = d // g * g
la -= d1
ra -= d1
while la < lb:
    la += g
    ra += g
while la >= lb:
    la -= g
    ra -= g


def work():
    x0 = max(la, lb)
    x1 = min(ra, rb)
    r = x1 - x0 + 1
    return r


res = 0
res = max(work(), res)
while la < lb:
    la += g
    ra += g
res = max(work(), res)
print(res)
