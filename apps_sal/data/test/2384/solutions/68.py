
def resolve():
    INF = float("-inf")
    N = int(input())
    A = list(map(int, input().split()))

    skip = 1 + N % 2
    # i番目までの要素を見たときに、ｊ個選ばない時の最大値
    dp = [[INF] * (skip + 2) for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(skip + 1):  # j: スキップする個数
            # 今見ている要素をスキップ
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])
            now = dp[i][j]
            if (i + j) % 2 == 0:
                now += A[i]
            dp[i + 1][j] = max(dp[i + 1][j], now)

    print(dp[N][skip])


def __starting_point():
    resolve()


__starting_point()
