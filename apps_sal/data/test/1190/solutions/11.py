import collections
import atexit
import math
import sys
import bisect
sys.setrecursionlimit(1000000)
isdebug = False
try:
    import pywin32
    import numpy

    def dprint(*args, **kwargs):
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
            sys.stdin = f
        except Exception:
            dprint('invalid input file')
    if outId > 0:
        dprint('use output', outId)
        try:
            f = open('stdout' + str(outId) + '.txt', 'w')
            sys.stdout = f
        except Exception:
            dprint('invalid output file')
        atexit.register(lambda: sys.stdout.close())


if isdebug:
    red_inout()


def getIntList():
    return list(map(int, input().split()))


def solve():
    pass


T_ = 1
for iii_ in range(T_):
    (w1, h1, w2, h2) = getIntList()
    r = w1 + 2
    r += 2 * h1
    r += w2 + 2
    r += 2 * h2
    r += w1 - w2
    print(r)
