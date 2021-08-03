def main():
    n, ma, mb = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [{} for _ in range(n + 1)]
    dp[0][(0, 0)] = 0
    for i in range(n):
        for ky in dp[i].keys():
            if ky in dp[i + 1]:
                if dp[i + 1][ky] > dp[i][ky]:
                    dp[i + 1][ky] = dp[i][ky]
            else:
                dp[i + 1][ky] = dp[i][ky]
            t = (ky[0] + arr[i][0], ky[1] + arr[i][1])
            if t in dp[i + 1]:
                if dp[i + 1][t] > dp[i][ky] + arr[i][2]:
                    dp[i + 1][t] = dp[i][ky] + arr[i][2]
            else:
                dp[i + 1][t] = dp[i][ky] + arr[i][2]
    ans = float("inf")
    for i in range(1, 41):
        t = (ma * i, mb * i)
        if t in dp[n]:
            if ans > dp[n][t]:
                ans = dp[n][t]
    if ans == float("inf"):
        print("-1")
    else:
        print(ans)


def __starting_point():
    main()


__starting_point()
