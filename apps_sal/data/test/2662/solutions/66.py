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


def main():
    n = I()
    _l = [I() for _ in range(n)]
    l = collections.deque()

    for A in _l:
        if len(l) == 0:
            l.append(A)
            continue

        lv = l[0]
        rv = l[-1]
        if rv < A:
            l[-1] = A
            continue
        if A <= lv:
            l.appendleft(A)
            continue

        li = 0
        ri = len(l) - 1
        while ri - li > 1:
            mi = (ri + li) // 2
            if l[mi] < A:
                li = mi
            else:
                ri = mi

        l[li] = A

    # print(l)
    return len(l)


# main()
print((main()))
