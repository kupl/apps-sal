k, pa, pb = list(map(int, input().split()))

MOD = 10**9 + 7
INF = ((pa + pb) * pow(pb, MOD - 2, MOD)) % MOD
rAB = pow(pa + pb, MOD - 2, MOD)
rB = pow(pb, MOD - 2, MOD)

memo = {}


def dfs(a, ab):
    if ab >= k:
        return ab
    if a + ab >= k:
        return ((a + MOD - 1) + (pa + pb) * rB + ab) % MOD
        return a - 1 + (pa + pb) / pb + ab
    if (a, ab) in memo:
        return memo[a, ab]
    res = (dfs(a + 1, ab) * pa * rAB) + (dfs(a, ab + a) * pb * rAB)
    memo[a, ab] = res = res % MOD
    return res


print(dfs(1, 0))
