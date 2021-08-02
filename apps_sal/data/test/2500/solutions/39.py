def xor_sum(N: int) -> int:
    MOD = 10**9 + 7

    digits = len(bin(N)) - 2

    dp = [[0] * 3 for _ in range(digits + 1)]
    dp[0][0] = 1

    for i in range(digits):
        if N >> (digits - 1 - i) & 1:
            dp[i + 1][0] = dp[i][0]
            dp[i + 1][1] = (dp[i][0] + dp[i][1]) % MOD
            dp[i + 1][2] = (dp[i][1] * 2 + dp[i][2] * 3) % MOD
        else:
            dp[i + 1][0] = (dp[i][0] + dp[i][1]) % MOD
            dp[i + 1][1] = dp[i][1]
            dp[i + 1][2] = (dp[i][1] + dp[i][2] * 3) % MOD

    return sum(dp[digits]) % MOD


def __starting_point():
    N = int(input())
    ans = xor_sum(N)
    print(ans)


__starting_point()
