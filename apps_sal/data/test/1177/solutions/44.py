def main():
    n, s, *a = list(map(int, open(0).read().split()))
    ans = 0
    mod = 998244353
    dp = [0] * (s + 1)
    for i, x in enumerate(a):
        dp[0] += 1
        if x > s:
            continue
        ans += dp[s - x] * (n - i)
        ans %= mod
        dp = dp[:x] + [(dp[j] + dp[j - x]) % mod for j in range(x, s + 1)]
    print(ans)


def __starting_point():
    main()


__starting_point()
