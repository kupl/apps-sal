import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15


def main():
    (H, W) = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [list(map(int, input().split())) for _ in range(H)]
    dp = [[0] * (1 + W) for _ in range(H + 1)]
    x = abs(A[0][0] - B[0][0])
    dp[0][0] = 1 << 12800 + x
    dp[0][0] |= 1 << 12800 - x
    for i in range(H):
        for j in range(W):
            c = abs(A[i][j] - B[i][j])
            if i > 0:
                dp[i][j] |= dp[i - 1][j] << c
                dp[i][j] |= dp[i - 1][j] >> c
            if j > 0:
                dp[i][j] |= dp[i][j - 1] << c
                dp[i][j] |= dp[i][j - 1] >> c
    ans = INF
    x = dp[H - 1][W - 1]
    for i in range(25600):
        if x & 1:
            ans = min(ans, abs(i - 12800))
        x >>= 1
    print(ans)


def __starting_point():
    main()


__starting_point()
