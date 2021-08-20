def main():
    MOD = 998244353
    (N, S) = list(map(int, input().split()))
    (*A,) = list(map(int, input().split()))
    dp = [0] * (S + 1)
    ans = 0
    for x in A:
        dp[0] += 1
        for j in range(S, x - 1, -1):
            dp[j] = (dp[j] + dp[j - x]) % MOD
        ans = (ans + dp[S]) % MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
