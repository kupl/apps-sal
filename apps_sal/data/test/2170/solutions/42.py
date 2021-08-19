def main():
    (n, m) = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    fact = [1]
    fact_inv = [1]
    for i in range(m):
        fact.append(fact[-1] * (i + 1) % MOD)
    fact_inv = [1] * (m + 1)
    fact_inv[m] = pow(fact[m], MOD - 2, MOD)
    for i in range(m):
        fact_inv[m - i - 1] = fact_inv[m - i] * (m - i) % MOD
    mPn = fact[m] * pow(fact[m - n], MOD - 2, MOD) % MOD
    a = pow(mPn, 2, MOD)
    b = 0
    for i in range(1, n + 1):
        nCr = fact[n] * fact_inv[i] % MOD * fact_inv[n - i] % MOD
        b += (-1) ** (i % 2) * nCr * fact[m - i] % MOD * fact_inv[m - n] % MOD
        b %= MOD
    ans = a + b * mPn
    print(ans % MOD)


main()
