#
import collections
import atexit
import math
import sys
import bisect

sys.setrecursionlimit(1000000)


def getIntList():
    return list(map(int, input().split()))


try:
    #raise ModuleNotFoundError
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
    sys.stdin = open('input' + str(inId) + '.txt', 'r')  # 标准输出重定向至文件
if outId > 0:
    dprint('use output', outId)
    sys.stdout = open('stdout' + str(outId) + '.txt', 'w')  # 标准输出重定向至文件
    atexit.register(lambda: sys.stdout.close())  # idle 中不会执行 atexit

N, = getIntList()
za = getIntList()

M, = getIntList()
zb = getIntList()

if sum(za) != sum(zb):
    print(-1)
    return

ia = 0
ib = 0
ta = 0
tb = 0
r = N
while ia < N or ib < M:
    if ta == tb:
        if ia == N:
            break
        ta = za[ia]
        tb = zb[ib]
        ia += 1
        ib += 1

    elif ta < tb:
        ta += za[ia]
        ia += 1
        r -= 1
    else:
        tb += zb[ib]
        ib += 1

print(r)
