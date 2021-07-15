def main():
    N, S = list(map(int, input().split()))
    A = list(map(int, input().split()))
    return solve(N, S, A)

def solve(N, S, A):
    mod = 998244353
    dp = [0] * (S + 1)
    dp[0] = pow(2, N, mod)
    div2 = pow(2, mod - 2, mod)
    m = 0
    for a in A:
        m += a
        for i in reversed(list(range(a, min(S, m) + 1))):
            dp[i] = (dp[i] + dp[i - a] * div2) % mod
    return dp[S]

print((main()))

