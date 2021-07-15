import numpy as np

MOD = 998244353

def solve(A,S):
    N = len(A)
    dp = np.zeros(S+1, dtype=int)
    res = 0
    for i,a in enumerate(A):
        if a > S:
            continue
        res += dp[S-a]*(N-i)
        res %= MOD
        dp[a:] += dp[:-a]
        dp[a] += i+1
        dp %= MOD
    for i,a in enumerate(A):
        if a == S:
            res += (i+1)*(N-i)
            res %= MOD

    return res%MOD


def __starting_point():
    N,S = map(int,input().split())

    A = tuple(map(int,input().split()))

    print(solve(A,S))
__starting_point()
