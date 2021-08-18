import bisect
import collections
import copy
import itertools
import math
import string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip.split())


def main():
    n = I()
    h = LI()
    ok = 0
    ng = 0
    ans = 0

    for i, x in enumerate(h):
        if x > 0:
            ok = i
            break
    else:
        ok = n

    while ok != n:
        for i, x in enumerate(h[ok + 1:]):
            if x == 0:
                ng = ok + 1 + i
                break
        else:
            ng = n
        sub = [0] * ok + [1] * (ng - ok) + [0] * (n - ng)

        for i in range(n):
            h[i] -= sub[i]
        for i, x in enumerate(h):
            if x > 0:
                ok = i
                break
            else:
                ok = n
        ans += 1

    print(ans)


main()
