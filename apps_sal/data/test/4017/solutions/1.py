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
(N,) = getIntList()
za = getIntList()
ss = sum(za)
cc = collections.Counter(za)
re = []
for i in range(N):
    if (ss - za[i]) % 2 == 1:
        continue
    t = (ss - za[i]) // 2
    g = 1
    if t == za[i]:
        g += 1
    if cc[t] >= g:
        re.append(str(i + 1))
print(len(re))
print(' '.join(re))
