#!python3

# input
N = int(input())
A = list(map(int, input().split()))
# N = 2000
# A = [i for i in range(1, N + 1)]


def main():
    P = [(A[i], i + 1) for i in range(N)]
    P.sort(reverse=True)

    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for n, p in zip(list(range(1, N + 1)), P):
        x, y = p
        for i in range(n):
            j = n - 1 - i
            left = dp[i][j] + x * abs(y - (i + 1))
            dp[i + 1][j] = max(dp[i + 1][j], left)
            right = dp[i][j] + x * abs(y - (N - j))
            dp[i][j + 1] = max(dp[i][j + 1], right)

    ans = max([dp[i][N - i] for i in range(N)])
    print(ans)


def __starting_point():
    main()

__starting_point()
