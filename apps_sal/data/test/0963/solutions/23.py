MOD = 998244353


def solve(n, k, l, r):
    dp = [0] * n
    dp[0] = 1
    memo = [1] * n
    for i in range(1, n):
        v = 0
        for x, y in zip(l, r):
            a = i - x
            if a < 0:
                continue
            v += memo[a]
            b = i - y - 1
            if b < 0:
                continue
            v -= memo[b]
        dp[i] = v % MOD
        memo[i] = (memo[i - 1] + dp[i]) % MOD
    return dp[n - 1]


n, k = list(map(int, input().split()))
l, r = list(zip(*[list(map(int, input().split())) for i in range(k)]))
print((solve(n, k, l, r)))
