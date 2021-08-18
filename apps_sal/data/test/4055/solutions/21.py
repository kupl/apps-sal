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
za = getIntList()

re = 0

for i in range(1, N - 1):
    if za[i] == 0 and za[i - 1] == 1 and za[i + 1] == 1:
        re += 1
        za[i + 1] = 0

print(re)
