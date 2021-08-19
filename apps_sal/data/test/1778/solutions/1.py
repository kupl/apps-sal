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
z1 = getIntList()
z2 = getIntList()

z1.sort()
z2.sort()

t1 = N - 1
t2 = N - 1
s1 = 0
s2 = 0


def bigone():
    if t1 >= 0 and t2 >= 0:
        if z1[t1] > z2[t2]:
            return 1
        else:
            return 2
    if t1 >= 0:
        return 1
    return 2


while t1 >= 0 or t2 >= 0:
    t = bigone()
    if t == 1:
        s1 += z1[t1]
        t1 -= 1
    else:
        t2 -= 1
    t = bigone()
    if t == 1:
        t1 -= 1
    else:
        s2 += z2[t2]
        t2 -= 1

print(s1 - s2)
