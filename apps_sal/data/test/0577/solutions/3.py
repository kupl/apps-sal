#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list([int(x)-1 for x in input().split()])
def II(): return int(input())
def IF(): return float(input())
def S(): return input().rstrip()
def LS(): return S().split()
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#solve
def solve():
    n, k = LI()
    ab = LIR(n)
    dp = [False] * k
    dp[0] = True
    A = 0
    B = 0
    for a, b in ab:
        ndp = dp[::1]
        A += a
        B += b
        for i in range(k):
            if dp[i]:
                for j in range(max((k - a), 1), min(k, (b + 1))):
                    ndp[(i+j)%k] = True
        dp = ndp[::1]
    ans = A // k + B // k
    for i in range(k):
        if dp[i]:
            ans = max(ans, (A + i) // k + (B - i) // k)
    print(ans)
    return


#main
def __starting_point():
    solve()

__starting_point()
