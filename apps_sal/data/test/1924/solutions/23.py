def main():
    mod = 10 ** 9 + 7
    N = 2 * 10 ** 6 + 3

    fac = [0] * N
    finv = [0] * N
    inv = [0] * N

    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, N):
        fac[i] = fac[i - 1] * i % mod
    finv[N // 2] = pow(fac[N // 2], mod - 2, mod)
    for i in reversed(list(range(N // 2))):
        finv[i] = (finv[i + 1] * (i + 1)) % mod

    def com(r, c):
        ans = fac[r + c] * finv[r] * finv[c]
        return ans % mod

    def g(r, c):
        return (com(r + 1, c + 1) - 1) % mod

    r1, c1, r2, c2 = list(map(int, input().split()))

    answer = g(r2, c2) - g(r2, c1 - 1) - g(r1 - 1, c2) + g(r1 - 1, c1 - 1)
    answer %= mod
    print(answer)


def __starting_point():
    main()


__starting_point()
