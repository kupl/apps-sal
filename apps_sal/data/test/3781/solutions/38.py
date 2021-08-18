from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())


def IR(n):
    return [I() for _ in range(n)]


def LIR(n):
    return [LI() for _ in range(n)]


sys.setrecursionlimit(1000000)
mod = 1000000007

ans = ["Second", "First"]


def solve():
    def f(n, a):
        if n & 1:
            return ans[0]
        cnt = defaultdict(lambda: 0)
        for i in a:
            cnt[i] ^= 1
        return ans[any(cnt.values())]

    t = I()
    for _ in range(t):
        n = I()
        a = LI()
        print((f(n, a)))
    return


def __starting_point():
    solve()


__starting_point()
