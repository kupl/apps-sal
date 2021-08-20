def sport(v):
    return v >= 2


def contest(v):
    return v in [1, 3]


LAST_CONTEST = 0
LAST_SPORT = 1


def __starting_point():
    n = int(input())
    a = list(map(int, input().split()))
    prev = [0, 0]
    dp = [0, 0]
    for i in range(n):
        v = a[i]
        curr = [dp[0], dp[1]]
        if sport(v):
            curr[LAST_SPORT] = max(dp[LAST_SPORT], 1 + prev[LAST_SPORT], 1 + dp[LAST_CONTEST])
        if contest(v):
            curr[LAST_CONTEST] = max(dp[LAST_CONTEST], 1 + prev[LAST_CONTEST], 1 + dp[LAST_SPORT])
        prev = dp
        dp = curr
    print(n - max(dp))


__starting_point()
