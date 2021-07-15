import typing
import sys
import math
import collections
import bisect
import itertools
import heapq
import decimal
import copy
import operator

# sys.setrecursionlimit(10000001)
INF = 10 ** 20
MOD = 10 ** 9 + 7
# MOD = 998244353
# buffer.readline()


def ni(): return int(sys.stdin.readline())
def ns(): return list(map(int, sys.stdin.readline().split()))
def na(): return list(map(int, sys.stdin.readline().split()))
def na1(): return list([int(x)-1 for x in sys.stdin.readline().split()])


# ===CODE===

def main():
    n, a, b = ns()

    res = collections.deque()
    if a+b > n+1:
        print((-1))
        return

    flg = a < b
    a, b = max(a, b), min(a, b)

    head = [i+1 for i in range(b)]
    head.reverse()
    tail = []

    remain = n-b-a+1
    if remain < 0:
        print((-1))
        return

    v = b+1
    for i in range(a-1):
        tmp = [v]
        v += 1
        while len(tmp) < b and remain > 0:
            tmp.append(v)
            v += 1
            remain -= 1
        tmp.reverse()
        tail += tmp

    if remain != 0:
        print((-1))
        return

    res = head+tail
    if flg:
        for i in range(n):
            res[i] = n+1-res[i]
    print((*res))


def __starting_point():
    main()

__starting_point()
