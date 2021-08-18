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

N, = getIntList()
S = input()

s0 = 'RGB' * 100000
s1 = 'RBG' * 100000
s2 = 'BRG' * 100000
s3 = 'BGR' * 100000
s4 = 'GRB' * 100000
s5 = 'GBR' * 100000

zs = [s0, s1, s2, s3, s4, s5]
zr = []
for x in zs:
    t = 0
    for i in range(N):
        if x[i] != S[i]:
            t += 1
    zr.append(t)

r = min(zr)
dprint(r)
for i in range(6):
    if zr[i] == r:
        print(r)
        print(zs[i][:N])
        break
