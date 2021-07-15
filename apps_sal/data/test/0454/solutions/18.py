N, K = map(int, input().split())
MOD = 10**9 + 7
memo = {}
def dfs(i, a, b, k):
    key = (i, a, b, k)
    if key in memo:
        return memo[key]
    if i == N:
        if b > 0:
            memo[key] = 0
            return 0
        return k == K
    r = dfs(i+1, a, b, k+a+b) + dfs(i+1, a+1, b+1, k+a+b+2)
    if a > 0:
        r += dfs(i+1, a, b, k+a+b) * a
    if b > 0:
        r += dfs(i+1, a, b, k+a+b) * b
    if a > 0 < b:
        r += dfs(i+1, a-1, b-1, k+a+b-2) * (a * b)
    memo[key] = r = r % MOD
    return r
print(dfs(0, 0, 0, 0))
