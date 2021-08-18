import sys
input = sys.stdin.readline
INF = float("inf")


def main():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    cost = [-1, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for aj in a:
            if i - cost[aj] < 0:
                continue
            dp[i] = max(dp[i], dp[i - cost[aj]] + 1)
    digits = dp[n]
    ans = ""
    rest = n
    while digits:
        for aj in a:
            if rest - cost[aj] < 0:
                continue
            if dp[rest - cost[aj]] == digits - 1:
                ans += str(aj)
                rest -= cost[aj]
                digits -= 1
                break
    print(ans)


def __starting_point():
    main()


__starting_point()
