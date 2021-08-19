import sys
input = sys.stdin.readline


def solve(N, K, L):
    dp = [[[0] * (K + 1) for _ in range(2)] for _ in range(L + 1)]
    dp[0][0][0] = 1
    for i in range(L):
        D = N[i]
        for j in range(2):
            d_max = 9 if j == 1 else D
            for k in range(K + 1):
                if k < K:
                    for d in range(d_max + 1):
                        dp[i + 1][int(j or d < D)][k + int(d > 0)] += dp[i][j][k]
                else:
                    dp[i + 1][j][k] += dp[i][j][k]
    return dp[L][0][K] + dp[L][1][K]


def main():
    N = list(map(int, input().rstrip()))
    K = int(input())
    L = len(N)
    ans = solve(N, K, L)
    print(ans)


def __starting_point():
    main()


__starting_point()
