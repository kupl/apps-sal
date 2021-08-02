import sys
input = sys.stdin.readline


def main():
    MOD = 10**9 + 7
    S = int(input())
    dp = [0 for i in range(S + 1)]
    dp[0] = 1

    for i in range(S + 1):
        for j in range(3, S + 1):
            if i + j > S:
                break
            dp[i + j] += dp[i]
            dp[i + j] %= MOD

    print(dp[-1])


def __starting_point():
    main()


__starting_point()
