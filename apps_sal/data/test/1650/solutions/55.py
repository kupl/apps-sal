import sys
MOD = 10 ** 9 + 7
INF = 10 ** 11
sys.setrecursionlimit(100000000)


def main():
    L = input()
    dp = [[0] * 2 for _ in range(len(L) + 1)]
    dp[0][0] = 1
    for i in range(len(L)):
        if L[i] == '1':
            dp[i + 1][0] = dp[i][0] * 2
            dp[i + 1][1] = dp[i][0] + dp[i][1] * 3
        else:
            dp[i + 1][0] = dp[i][0]
            dp[i + 1][1] = dp[i][1] * 3
        dp[i + 1][0] %= MOD
        dp[i + 1][1] %= MOD
    print(sum(dp[-1]) % MOD)


def __starting_point():
    main()


__starting_point()
