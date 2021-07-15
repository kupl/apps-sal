import math


def main():
    n = int(input())
    slices = [int(x) for x in input().split()]
    dp = [[[0,0], [0,0]] for i in range(n)]
    dp[-1][0] = [slices[-1], 0]
    dp[-1][1] = [0, slices[-1]]
    for i in range(n-2, -1, -1):
        for j in range(0, 2):
            take = slices[i] + dp[i+1][1-j][j]
            do_not_take = dp[i+1][j][j]
            if take > do_not_take:
                dp[i][j][j] = take
                dp[i][j][1-j] = dp[i+1][1-j][1-j]
            else:
                dp[i][j][j] = do_not_take
                dp[i][j][1-j] = slices[i] + dp[i+1][j][1-j]
    print(dp[0][1][0], dp[0][1][1])


def __starting_point():
    main()

__starting_point()
