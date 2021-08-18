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
re = 1
mc = 1
zc = []
for i in range(2, 10000):
    if N % i != 0:
        continue
    re *= i
    c = 0
    while N % i == 0:
        N //= i
        c += 1

    zc.append(c)
if N > 1:
    re *= N
    zc.append(1)
if zc:
    mc = max(zc)
t = 1
for i in range(100):
    if mc <= t:
        break
    t *= 2
dprint(t)
dprint(zc)
g = i
for x in zc:
    if x < t:
        g += 1
        break

print(re, g)
