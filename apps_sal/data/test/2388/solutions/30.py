from bisect import bisect
from itertools import accumulate
from functools import reduce
from sys import setrecursionlimit

setrecursionlimit(10000000)

MOD = 998244353

def solve(robots):
    N = len(robots)
    robots.sort()

    parent = [None]*(N+1)

    stack = [(float('inf'),0)]
    for i,(x,d) in enumerate(robots,start=1):
        d += x
        while stack[-1][0] <= x:
            stack.pop()
        parent[i] = stack[-1][1]
        while stack[-1][0] <= d:
            stack.pop()
        stack.append((d,i))

    dp = [1]*(N+1)
    for i in reversed(range(1,N+1)):
        p = parent[i]
        dp[p] *= dp[i]+1
        dp[p] %= MOD
    return dp[0]

def __starting_point():
    N = int(input())
    robots = [tuple(map(int,input().split())) for _ in range(N)]
    print(solve(robots))
__starting_point()
