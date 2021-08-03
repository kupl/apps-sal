from collections import *
import sys
try:
    inp = raw_input
except:
    inp = input


def err(s):
    sys.stderr.write('{}\n'.format(s))


def ni():
    return int(inp())


def nl():
    return [int(_) for _ in inp().split()]


def solve():
    N, X = nl()
    A = nl()
    A.sort(reverse=True)
    SUM = 0
    NO = 0
    for a in A:
        SUM += a
        NO += 1
        if SUM < X * NO:
            print(NO - 1)
            return
    print(N)


T = ni()
for _ in range(T):
    solve()
