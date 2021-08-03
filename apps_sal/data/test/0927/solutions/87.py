import sys

input = sys.stdin.readline


def main():
    N, M = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]

    match = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]

    dp = [0] * (N + 1)

    for i in range(1, N + 1):
        for a in A:
            if match[a] <= i:
                if match[a] == i or dp[i - match[a]] != 0:
                    dp[i] = max(dp[i], dp[i - match[a]] * 10 + a)

    print((dp[-1]))


def __starting_point():
    main()


__starting_point()
