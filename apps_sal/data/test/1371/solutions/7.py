

def main():
    import sys
    input = sys.stdin.readline

    s = int(input())
    mod = 10 ** 9 + 7
    dp = [0 for _ in range(s + 1)]
    dp[0] = 1

    for i in range(1, s + 1):
        for j in range(i - 3 + 1):
            dp[i] += dp[j]
            dp[i] %= mod

    print((dp[s]))


def __starting_point():
    main()


__starting_point()
