t = int(input())

dp = [[[0 for i in range(51)] for j in range(31)] for k in range(31)]


def cost(n, m, k):
    if (dp[n][m][k] or k == 0 or n * m == k):
        return dp[n][m][k]
    c = 10**9
    for i in range(1, n // 2 + 1):
        for j in range(k + 1):
            c = min(c, cost(n - i, m, k - j) + cost(i, m, j) + m * m)
    for i in range(1, m // 2 + 1):
        for j in range(k + 1):
            c = min(c, cost(n, m - i, k - j) + cost(n, i, j) + n * n)
    dp[n][m][k] = c
    return c


for _ in range(t):
    n, m, k = list(map(int, input().split()))
    print(cost(n, m, k))
