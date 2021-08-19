def resolve():
    (n, s) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    mod = 998244353
    modinv = pow(2, mod - 2, mod)
    dp = [0] * (s + 1)
    dp[0] = pow(2, n, mod)
    for i in a:
        for j in range(s - i, -1, -1):
            dp[j + i] += dp[j] * modinv
            dp[j + i] %= mod
    print(dp[-1])


def __starting_point():
    resolve()


__starting_point()
