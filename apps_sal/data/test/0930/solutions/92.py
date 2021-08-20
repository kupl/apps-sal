def main():
    (n, kk) = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    fact = [1, 1]
    for i in range(2, 2 * 10 ** 5 + 1):
        fact.append(fact[-1] * i % mod)

    def nCr(n, r, mod=10 ** 9 + 7):
        return pow(fact[n - r] * fact[r] % mod, mod - 2, mod) * fact[n] % mod
    ans = [1]
    for k in range(1, n):
        ans.append(nCr(n - 1, k) * nCr(n, k) % mod)
    print(sum(ans[:min(kk + 1, n)]) % mod)


main()
