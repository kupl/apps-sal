def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(enumerate(A), key=lambda x: x[1])[::-1]
    dp = [[0] * (N + 1 - i) for i in range(N + 1)]
    m = 0
    for i in range(1, len(A) + 1):
        (index, a) = A[i - 1]
        for j in range(i + 1):
            if (i - j, j) == (0, 0):
                dp[i - j][j] = 0
            elif i - j == 0:
                dp[i - j][j] = dp[i - j][j - 1] + (N - j - index) * a
            elif j == 0:
                dp[i - j][j] = dp[i - j - 1][j] + abs(index - (i - j - 1)) * a
            else:
                dp[i - j][j] = max(dp[i - j][j - 1] + (N - j - index) * a, dp[i - j - 1][j] + abs(index - (i - j - 1)) * a)
            if i == len(A):
                m = max(m, dp[i - j][j])
    print(m)


main()
