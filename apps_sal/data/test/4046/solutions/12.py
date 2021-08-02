#
import collections
import atexit
import math
import sys
import bisect

sys.setrecursionlimit(1000000)

isdebug = False
try:
    #raise ModuleNotFoundError
    import pylint
    import numpy

    def dprint(*args, **kwargs):
        #print(*args, **kwargs, file=sys.stderr)
        # in python 3.4 **kwargs is invalid???
        print(*args, file=sys.stderr)
    dprint('debug mode')
    isdebug = True
except Exception:
    def dprint(*args, **kwargs):
        pass


def red_inout():
    inId = 0
    outId = 0
    if not isdebug:
        inId = 0
        outId = 0
    if inId > 0:
        dprint('use input', inId)
        try:
            f = open('input' + str(inId) + '.txt', 'r')
            sys.stdin = f  # 标准输出重定向至文件
        except Exception:
            dprint('invalid input file')
    if outId > 0:
        dprint('use output', outId)
        try:
            f = open('stdout' + str(outId) + '.txt', 'w')
            sys.stdout = f  # 标准输出重定向至文件
        except Exception:
            dprint('invalid output file')

        atexit.register(lambda: sys.stdout.close())  # idle 中不会执行 atexit


if isdebug and len(sys.argv) == 1:
    red_inout()


def getIntList():
    return list(map(int, input().split()))


def solve():
    pass


T_ = 1
#T_, = getIntList()

for iii_ in range(T_):
    # solve()
    N, = getIntList()
    # print(N)
    zd = getIntList()
    tot = 0
    big = -1
    for x in zd:
        tot += x
        big = max(big, tot)
    if big < -1 or big == 0 or big >= N:
        print(-1)
        break
    if big < 0:
        a = N
    else:
        a = N - big
    zr = [a for i in range(N)]
    vis = [False for i in range(N + 1)]
    vis[a] = True
    ok = True
    for i in range(1, N):
        zr[i] = zr[i - 1] + zd[i - 1]
        if zr[i] < 1 or zr[i] > N:
            ok = False
            break
        if (vis[zr[i]]):
            ok = False
            break
        vis[zr[i]] = True
    if not ok:
        print(-1)
        break
    for i in range(N):
        zr[i] = str(zr[i])
    r = ' '.join(zr)
    print(r)
