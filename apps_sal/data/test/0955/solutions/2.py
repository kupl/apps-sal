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

N, = getIntList()

dp = [10 ** 10 for i in range(10)]
dp[0] = 0
for _ in range(N):
    g = input().split()
    p = int(g[0])
    v = g[1]
    t = 0
    c = 0
    for x in 'ABC':
        if x in v:
            t = t | (1 << c)
        c += 1
    for i in range(8):
        if dp[i] + p < dp[i | t]:
            dp[i | t] = dp[i] + p

if dp[7] == 10 ** 10:
    print(-1)
else:
    print(dp[7])
