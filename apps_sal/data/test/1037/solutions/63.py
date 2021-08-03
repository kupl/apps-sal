
def main():

    n = int(input())
    arr = list(map(int, input().split()))
    arr = tuple(sorted(enumerate(arr), key=lambda tpl: -tpl[1]))

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i, (p, a) in enumerate(arr):
        for l in range(i + 1):
            dp[i + 1][l] = max(dp[i + 1][l], dp[i][l] + a * abs(p - (n - (i - l) - 1)))
            dp[i + 1][l + 1] = max(dp[i + 1][l + 1], dp[i][l] + a * abs(p - l))

    print((max(dp[n])))


main()
