import collections
import atexit
import math
import sys
import bisect
sys.setrecursionlimit(1000000)


def getIntList():
    return list(map(int, input().split()))


isdebug = False
try:
    import numpy

    def dprint(*args, **kwargs):
        print(*args, file=sys.stderr)
    dprint('debug mode')
    isdebug = True
except Exception:

    def dprint(*args, **kwargs):
        pass
inId = 0
outId = 0
if not isdebug:
    inId = 0
    outId = 0
if inId > 0:
    dprint('use input', inId)
    try:
        f = open('input' + str(inId) + '.txt', 'r')
        sys.stdin = f
    except Exception:
        dprint('invalid input file')
if outId > 0:
    dprint('use output', outId)
    try:
        f = open('stdout' + str(outId) + '.txt', 'w')
        sys.stdout = f
    except Exception:
        dprint('invalid output file')
    atexit.register(lambda: sys.stdout.close())
(N, M, K) = getIntList()
za = getIntList()
dprint(za)
za.sort()
a = za[-1]
b = za[-2]
r = 0
t = M // (K + 1)
r = t * (a * K + b)
r += M % (K + 1) * a
print(r)
