def solve(n, k, l):
    dp = [[0] * n for _ in range(n + 1)]
    m = 0
    for i in range(1, n + 1):
        for j in range(n):
            if i + j - 1 >= len(l):
                continue
            dp[i][j] = dp[i - 1][j] + l[i + j - 1]
            if i >= k:
                m = max(m, dp[i][j] / i)
    return m


def __starting_point():
    n, k = list(map(int, input().split()))
    l = list(map(int, input().split()))
    print(solve(n, k, l))


__starting_point()
