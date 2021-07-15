def main():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = [[0] * 5 for _ in range(n)]
    dp[0] = [arr[0], arr[0] * x, 0]
    ans = max(dp[0])
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0] + arr[i], arr[i])
        dp[i][1] = max(dp[i - 1][0] + arr[i] * x, arr[i] * x, dp[i - 1][1] + arr[i] * x)
        dp[i][2] = max(dp[i - 1][2] + arr[i], dp[i - 1][1] + arr[i])
        ans = max(ans, max(dp[i]))
    print(ans)
    return 0

main()
