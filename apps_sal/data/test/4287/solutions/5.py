import math


def main():
    a, n, m = list(map(int, input().split()))
    rain = []
    u = []
    w = []
    raining = [False] * (a + 1)
    for i in range(n):
        l, r = list(map(int, input().split()))
        rain.append((l, r))
        for j in range(l, r):
            raining[j] = True

    for i in range(m):
        x, y = list(map(int, input().split()))
        u.append(x)
        w.append(y)

    rain_int = [0] * a
    for i in range(n):
        rain_int[rain[i][0] - 1] = 1
        rain_int[rain[i][1] - 1] = -1

    umbrellas = [-1 for _ in range(a + 1)]
    for i, x in enumerate(u):
        if umbrellas[x] == -1 or w[umbrellas[x]] > w[i]:
            umbrellas[x] = i

    dp = [[math.inf for _ in range(m + 1)] for _ in range(a + 1)]
    dp[0][m] = 0
    for i in range(a):
        for j in range(m + 1):
            if dp[i][j] == math.inf:
                continue
            if not raining[i]:
                dp[i + 1][m] = min(dp[i + 1][m], dp[i][j])
            if j < m:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + w[j])
            if umbrellas[i] != -1:
                dp[i + 1][umbrellas[i]] = min(dp[i + 1][umbrellas[i]], dp[i][j] + w[umbrellas[i]])

    ans = math.inf
    for i in range(m + 1):
        ans = min(ans, dp[a][i])
    print(-1 if ans == math.inf else ans)


def __starting_point():
    main()


__starting_point()
