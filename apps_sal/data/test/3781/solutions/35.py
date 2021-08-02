import math
import itertools
import fractions
import heapq
import collections
import bisect
import sys
import queue
import copy

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI(): return [int(x) for x in sys.stdin.readline().split()]
# def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

# Summarize count of factor within list -- START --


def summarizeList(l):
    sl = sorted(l)

    a = sl[0]
    c = 1
    res = []

    for x in sl[1:]:
        if x == a:
            c += 1
        else:
            res.append([a, c])
            a = x
            c = 1
    res.append([a, c])

    return res
# Summarize count of factor within list --- END ---


def main():
    ans = []
    N = I()
    for _ in range(N):
        n = I()
        l = LI()

        if n % 2 == 1:
            ans.append('Second')
        else:
            sl = summarizeList(l)
            f = True
            for x, c in sl:
                if c % 2 == 1:
                    f = False
            if f:
                ans.append('Second')
            else:
                ans.append('First')

    for x in ans:
        print(x)


main()
# print(main())
