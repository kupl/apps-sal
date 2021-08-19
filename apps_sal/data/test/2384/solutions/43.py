def main():
    INF = 10 ** 18
    N = int(input())
    A = list(map(int, input().split(' ')))
    K = 1 + N % 2  # 余分な×を入れられる個数
    # dp[i][j]: i個目までの要素で余分な×をj個使った際の最大値
    dp = [[- INF for _ in range(K + 1)] for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(K + 1):
            if j < K:
                # 余分な×を使う場合
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])
            # 余分な×を使わない場合
            now = dp[i][j]
            if (i + j) % 2 == 0:
                # 基本はi % 2 == 0の時にA[i]を足していく
                # ただ、余分な×がj個入っていると、その分ずれる
                now += A[i]
            dp[i + 1][j] = max(dp[i + 1][j], now)
    print((dp[N][K]))


def __starting_point():
    main()


__starting_point()
