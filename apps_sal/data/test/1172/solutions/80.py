import sys


def main():
    S = input()
    l = len(S)
    MOD = 10**9 + 7
    dp = [[0 for _ in range(3)] for _ in range(2)]
    cq = 1
    for st in S:
        if st == "A":
            dp[1][0] = dp[0][0] + cq
            dp[1][1] = dp[0][1]
            dp[1][2] = dp[0][2]
        elif st == "B":
            dp[1][0] = dp[0][0]
            dp[1][1] = dp[0][0] + dp[0][1]
            dp[1][2] = dp[0][2]
        elif st == "C":
            dp[1][0] = dp[0][0]
            dp[1][1] = dp[0][1]
            dp[1][2] = dp[0][1] + dp[0][2]
        else:
            dp[1][0] = dp[0][0] * 3 + cq
            dp[1][1] = dp[0][1] * 3 + dp[0][0]
            dp[1][2] = dp[0][2] * 3 + dp[0][1]
            cq *= 3
            cq %= MOD
        for i in range(3):
            dp[0][i] = dp[1][i] % MOD

    print((dp[0][-1]))


def __starting_point():
    main()


__starting_point()
