import collections
import atexit
import math
import sys
import bisect
sys.setrecursionlimit(1000000)
isdebug = False
try:
    import pylint
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


if isdebug and len(sys.argv) == 1:
    red_inout()


def getIntList():
    return list(map(int, input().split()))


def solve():
    pass


T_ = 1
for iii_ in range(T_):
    (N,) = getIntList()
    za = getIntList()
    la = 0
    big = 0
    for i in range(N):
        if za[i] == 1:
            la += 1
            big = max(la, big)
        else:
            la = 0
    r = big
    tot = 0
    for x in za:
        if x:
            tot += 1
        else:
            break
    for x in reversed(za):
        if x:
            tot += 1
        else:
            break
    r = max(tot, big)
    print(r)
