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


def memo(func):
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


@memo
def comb(n, k):
    if k > n:
        return 0
    if k == 0:
        return 1
    if n == k:
        return 1
    return comb(n - 1, k - 1) + comb(n - 1, k)


def getclam(K, left=3):
    if K == 0:
        return 1
    if left == 0:
        return 1
    s = str(K)
    l = len(s)

    r = 0
    x = int(s[0])
    if l > 1:
        for i in range(left + 1):
            r += comb(l - 1, i) * 9 ** i
        if x > 0:
            for i in range(left):
                r += comb(l - 1, i) * 9 ** i * (x - 1)
        s1 = s[1:]
        y = 0
        if s1:
            y = int(s1)
        if x != 0:
            left -= 1
        r += getclam(y, left)
        return r
    else:
        return x + 1


for i in range(1000, 1100):
    continue
    dprint(i, getclam(i))

for _ in range(N):
    L, R = getIntList()
    r = getclam(R) - getclam(L - 1)
    print(r)
