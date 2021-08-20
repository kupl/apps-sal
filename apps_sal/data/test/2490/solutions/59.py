import sys
input = sys.stdin.readline


def main():
    NS = input().strip('\n')[::-1]
    dp = [[0] * 2 for i in range(len(NS))]
    dp[0][0] = int(NS[0])
    dp[0][1] = 10 - int(NS[0])
    for i in range(1, len(NS)):
        d = int(NS[i])
        dp[i][0] = min(dp[i - 1][0] + d, dp[i - 1][1] + d + 1)
        dp[i][1] = min(dp[i - 1][0] + 10 - d, dp[i - 1][1] - 1 + 10 - d)
    dp[-1][1] += 1
    print(min(dp[-1]))


def __starting_point():
    main()


__starting_point()
