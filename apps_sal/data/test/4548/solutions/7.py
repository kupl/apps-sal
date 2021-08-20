import sys
input = sys.stdin.readline


def main():
    (n, m, x) = map(int, input().split())
    maps = []
    maps = list(map(int, input().split()))
    dp = [0] * (n + 1)
    left = 0
    right = 0
    for i in maps:
        dp[i] = 1
    left = sum(dp[x:])
    right = sum(dp[:x])
    print(min(left, right))


def __starting_point():
    main()


__starting_point()
