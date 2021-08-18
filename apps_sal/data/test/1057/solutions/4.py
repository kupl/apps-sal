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
s = input()

for a in range(1, 1000000):
    if s[a] != s[0]:
        break

for b in range(N - 2, -1, -1):
    if s[b] != s[N - 1]:
        break
dprint(a, b)
base = 998244353
if s[0] != s[N - 1]:
    print(a + N - b)
else:
    print((a + 1) * (N - b) % base)
