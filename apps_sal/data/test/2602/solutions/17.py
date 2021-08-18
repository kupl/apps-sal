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
        a, b, n, m = LI()
        if a + b < n + m:
            print("No")
            continue
        if a <= b:
            a, b = b, a
        r = a - b
        a -= min(n, r)
        n -= min(n, r)
        if a != b:
            if b < m:
                print("No")
            else:
                b -= m
                if n <= a + b:
                    print("Yes")
                else:
                    print("No")
        else:
            r = min(a, b, n, m)
            a -= r
            b -= r
            n -= r
            m -= r
            if a == 0:
                if n == m == 0:
                    print("Yes")
                else:
                    print("No")
            else:
                if m > a:
                    print("No")
                else:
                    print("Yes")
    return


def __starting_point():
    solve()


__starting_point()
