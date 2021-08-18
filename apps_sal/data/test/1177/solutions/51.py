
def main():
    MOD = 998244353

    N, S = list(map(int, input().split()))
    *a, = list(map(int, input().split()))

    dp = [0] * (S + 1)

    ret = 0
    for i, x in enumerate(a):
        dp[0] += 1
        if x > S:
            continue
        ret = (ret + dp[S - x] * (N - i)) % MOD
        for k in range(S - 1, x - 1, -1):
            dp[k] = (dp[k] + dp[k - x]) % MOD

    print(ret)


def __starting_point():
    main()


__starting_point()
