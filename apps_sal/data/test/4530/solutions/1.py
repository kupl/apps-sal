from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return [list(x) for x in sys.stdin.readline().split()]


def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res


def IR(n):
    return [I() for i in range(n)]


def LIR(n):
    return [LI() for i in range(n)]


def SR(n):
    return [S() for i in range(n)]


def LSR(n):
    return [LS() for i in range(n)]


sys.setrecursionlimit(1000000)
mod = 1000000007


def solve():
    t = I()
    for _ in range(t):
        n = I()
        a = LI()
        x = len(set(a))
        d = defaultdict(lambda: 0)
        for i in a:
            d[i] += 1
        y = max(d.values())
        if x < y:
            print(x)
        elif x == y:
            print(x - 1)
        else:
            print(y)
    return


def __starting_point():
    solve()


__starting_point()
