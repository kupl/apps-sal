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

N, L, R = getIntList()
# print(N)

base = 10 ** 9 + 7
#  1 2 3 4 5
g = R - L + 1
f = g // 3
zz = [f, f, f]
for i in range(g % 3):
    t = (i + L) % 3
    zz[t] += 1

dp = zz.copy()
dprint(dp)
for _ in range(1, N):
    dp1 = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            dp1[(i + j) % 3] += dp[i] * zz[j]
    for i in range(3):
        dp1[i] %= base
    dp = dp1
    dprint(dp)
print(dp[0])
