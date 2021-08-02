
def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted([(a, i) for i, a in enumerate(A)], reverse=True)

    # dp[i][j] := A が大きい順に i + j 個について、i 個を左詰めして、j 個を右詰めしたときのスコア
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        j = 0
        while i + j < N:
            a, idx = A[i + j]
            # 左に詰める場合
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + (idx - i) * a)
            # 右に詰める場合
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + ((N - 1 - j) - idx) * a)
            j += 1
    ans = 0
    for i in range(N + 1):
        ans = max(ans, dp[i][N - i])
    print(ans)


def __starting_point():
    resolve()


__starting_point()
