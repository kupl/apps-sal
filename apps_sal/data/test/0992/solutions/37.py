import sys
input = sys.stdin.readline

def solve():
    MOD = 998244353
    inv2 = pow(2, MOD-2, MOD)

    N, S = list(map(int, input().split()))
    As = list(map(int, input().split()))

    dp = [0] * (S+1)
    dp[0] = pow(2, N, MOD)
    for A in As:
        for k in reversed(list(range(S-A+1))):
            dp[k+A] += dp[k] * inv2
            dp[k+A] %= MOD

    print((dp[-1]))


solve()

