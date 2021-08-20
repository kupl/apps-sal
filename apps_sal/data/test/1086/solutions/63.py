def resolve():
    (H, W) = list(map(int, input().split()))
    A = [tuple(map(int, input().split())) for _ in range(H)]
    B = [tuple(map(int, input().split())) for _ in range(H)]
    Sub = [[0] * W for i in range(H)]
    for i in range(H):
        for j in range(W):
            Sub[i][j] = abs(A[i][j] - B[i][j])
    max_k = 80 * (H + W)
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1 << max_k + Sub[0][0] | 1 << max_k - Sub[0][0]
    for i in range(H):
        for j in range(W):
            d = Sub[i][j]
            if i:
                dp[i][j] |= dp[i - 1][j] << d | dp[i - 1][j] >> d
            if j:
                dp[i][j] |= dp[i][j - 1] << d | dp[i][j - 1] >> d
    ans = 10 ** 18
    for i in range(max_k * 2 + 1):
        if dp[H - 1][W - 1] & 1 << i:
            ans = min(ans, abs(max_k - i))
    print(ans)


def __starting_point():
    resolve()


__starting_point()
