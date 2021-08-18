dp = {0: 0, 1: 1}


def f(x):
    if x not in dp:
        dp[x] = f(int(x / 2)) * 2 + 1
    return dp[x]


dp2 = {(0, 0): 0}


def dfs(x, n):
    if (x, n) in dp2:
        return dp2[(x, n)]
    if x == 0 or n == 0:
        return 0

    if dp[x] < n:
        return x
    x2 = int(x / 2)
    fx2 = dp[x2]
    ret = dfs(x2, n)
    if n > fx2:
        ret += dfs(x2, n - fx2 - 1) + (x % 2)

    dp2[(x, n)] = ret
    return ret


n, l, r = list(map(int, input().split()))
f(n)
print(dfs(n, r) - dfs(n, l - 1))
