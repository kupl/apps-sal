def main():
    mod = 998244353
    n, s = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a = [i for i in a if i <= s]
    dp = [0 for i in range(s + 1)]
    half = pow(2, mod - 2, mod)
    for i in a:
        dp2 = [j for j in dp]
        dp2[i] = (dp2[i] + pow(2, n - 1, mod)) % mod
        for j in range(s - i + 1):
            dp2[j + i] = (dp2[j + i] + dp[j] * half) % mod
        dp = dp2
    print((dp[s]))


main()
