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
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()


def main():
    n = I()
    if n % 2 == 1 or n < 10:
        return 0

    st = 10
    ans = []
    while st <= n:
        ans.append(n // st)
        st *= 5

    return sum(ans)


print((main()))
