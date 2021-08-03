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
        #print(*args, **kwargs, file=sys.stderr)
        # in python 3.4 **kwargs is invalid???
        print(*args, file=sys.stderr)
    dprint('debug mode')
except Exception:
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

N, M = getIntList()

za = getIntList()
za.sort(reverse=True)

re = 0

for i in range(N - 1):
    a = za[i]
    b = za[i + 1]
    g = b
    if g >= a:
        t = a - 1
        if t < 1:
            t = 1
        re += g - t
        za[i + 1] = t
        re += a - 1
    else:
        re += g
print(re)
