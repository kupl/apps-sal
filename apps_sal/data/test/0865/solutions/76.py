import numpy as np
import sys
mod = 10**9 + 7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())


N, T = inpl()
dp = np.zeros((6001), int)
ABs = [inpl() for _ in range(N)]
ABs.sort()

for A, B in ABs:
    dp[A:T + A] = np.maximum(dp[A:T + A], dp[:T] + B)
    # for i in reversed(range(A,T+A)):
    #     dp[i] = max(dp[i-A] + B, dp[i])


print((max(dp)))
