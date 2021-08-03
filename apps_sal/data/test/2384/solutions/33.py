
def resolve():
    INF = float("-inf")
    N = int(input())
    A = list(map(int, input().split()))

    # 取る 取らない 取る 取らない ... を貪欲にやっていくと 1 + n % 2 個余って、
    # 1 + n % 2 回飛ばせることがわかる
    skip = 1 + N % 2

    # dp[i][j] := a[0, i) を j 要素無視して1つ飛びに取ったときの最大値
    dp = [[INF] * (skip + 1) for _ in range(N + 2)]
    dp[0][0] = 0
    for i in range(N + 1):
        for j in range(skip + 1):
            if j < skip:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])
            if i < N:
                dp[i + 2][j] = max(dp[i + 2][j], dp[i][j] + A[i])
    # 1個選んだら1個選ばないのもセット
    # なので floor(n / 2) * 2 + skip == n + 1 に答えが入る
    print((dp[N + 1][skip]))


def __starting_point():
    resolve()


__starting_point()
