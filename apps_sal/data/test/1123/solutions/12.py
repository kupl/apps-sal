MOD = 10**9 + 7


def mod_pow(p, q):
    res = 1
    while q > 0:
        if q & 1:
            res = (res * p) % MOD
        q //= 2
        p = (p * p) % MOD
    return res


def solve(n, k):
    dp = [0] * (k + 1)
    ans = 0
    for x in range(k, 0, -1):
        dp[x] = mod_pow((k // x), n) - sum(dp[y] for y in range(2 * x, k + 1, x))
        dp[x] %= MOD
        ans += dp[x] * x
    return ans % MOD


n, k = map(int, input().split())
print(solve(n, k))
