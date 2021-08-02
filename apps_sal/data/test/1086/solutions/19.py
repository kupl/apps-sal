import sys
input = sys.stdin.readline


def solve():
    maxV = 12800

    H, W = list(map(int, input().split()))
    Ass = [tuple(map(int, input().split())) for _ in range(H)]
    Bss = [tuple(map(int, input().split())) for _ in range(H)]

    dp = [[0] * (W) for _ in range(H)]
    diff = abs(Ass[0][0] - Bss[0][0])
    dp0 = 1 << maxV
    dp[0][0] = (dp0 << diff) | (dp0 >> diff)
    for i in range(H):
        for j in range(W):
            diff = abs(Ass[i][j] - Bss[i][j])
            if i > 0:
                dp0 = dp[i - 1][j]
                dp[i][j] |= (dp0 << diff) | (dp0 >> diff)
            if j > 0:
                dp0 = dp[i][j - 1]
                dp[i][j] |= (dp0 << diff) | (dp0 >> diff)

    ans = maxV
    dpHW = dp[-1][-1]
    for i in range(2 * maxV + 1):
        if (dpHW >> i) & 1:
            j = abs(i - maxV)
            if j < ans:
                ans = j

    print(ans)


solve()
