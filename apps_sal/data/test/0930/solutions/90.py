def main():
    n, k = list(map(int, input().split()))
    MOD = 10**9 + 7

    ans = 0
    k1 = 1
    k2 = 1
    for i in range(min(k + 1, n)):
        ans += k1 * k2
        ans %= MOD
        k1 *= (n - i) * pow(i + 1, MOD - 2, MOD)
        k1 %= MOD
        k2 *= (n - 1 - i) * pow(i + 1, MOD - 2, MOD)
        k2 %= MOD
    print((int(ans)))


main()
