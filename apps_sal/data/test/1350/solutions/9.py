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
        print(*args, **kwargs, file=sys.stderr)
    dprint('debug mode')
except ModuleNotFoundError:
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

N, K = getIntList()
zs = input()
t = {}
for x in zs:
    if x not in t:
        t[x] = 1
    else:
        t[x] += 1
ff = 100000
for y in t:
    ff = min(ff, t[y])
if len(t) < K:
    ff = 0
print(ff * K)
