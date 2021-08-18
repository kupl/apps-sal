import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    s = readline().rstrip().decode()
    n = len(s)
    P = int(1e9) + 7
    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = 1
    dp[0][1] = 2

    for i in range(1, n):
        if s[i] == '1':
            dp[i][0] += dp[i - 1][1] + dp[i - 1][0] * 3
            dp[i][1] += dp[i - 1][1] * 2

            dp[i][0] %= P
            dp[i][1] %= P
        else:
            dp[i][0] += dp[i - 1][0] * 3
            dp[i][1] += dp[i - 1][1]

            dp[i][0] %= P
            dp[i][1] %= P

    print(((dp[n - 1][0] + dp[n - 1][1]) % P))


def __starting_point():
    main()


__starting_point()
