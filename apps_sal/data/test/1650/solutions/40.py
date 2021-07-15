def main():
    l = list(input())
    n = len(l)
    dp = [[0,0] for _ in range(n+1)]
    dp[0][1] = 1
    for i in range(n):
        dp[i+1][0] += dp[i][0]*3
        if l[i] == '1':
            dp[i+1][1] += dp[i][1]*2
            dp[i+1][0] += dp[i][1]
        else:
            dp[i+1][1] += dp[i][1]
        dp[i+1][0] %= 10**9+7
        dp[i+1][1] %= 10**9+7
    print(sum(dp[n])%(10**9+7))

def __starting_point():
    main()
__starting_point()
