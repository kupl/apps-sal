import sys
input = sys.stdin.readline
P = 10 ** 9 + 7


def solve(L, N):
    dp = [[0, 0] for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        n = L[i]
        for j in range(2):
            max_d = 1 if j == 1 else n
            for d in range(max_d + 1):
                next_j = int(j or d < n)
                dp[i + 1][next_j] += (d + 1) * dp[i][j]
        dp[i + 1][0] %= P
        dp[i + 1][1] %= P
    return (dp[N][0] + dp[N][1]) % P


def main():
    L = list(map(int, input().rstrip()))
    N = len(L)
    ans = solve(L, N)
    print(ans)


def __starting_point():
    main()


__starting_point()
