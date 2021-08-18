def main():

    MOD = 10**9 + 7
    n, k = [int(c) for c in input().split()]
    f = [[None for j in range(n + 1)] for i in range(n + 1)]
    if k == 1:
        return 1

    nCr = [[0 for j in range(i + 1)] for i in range(n + 1)]
    nCr[0][0] = 1
    for i in range(1, n + 1):
        nCr[i] = [1] + [(nCr[i - 1][j] + nCr[i - 1][j - 1]) % MOD for j in range(1, i)] + [1]

    def powgen(base):
        this = 1
        while True:
            yield this
            this = this * base % MOD

    kpowgen, k1powgen = powgen(k), powgen(k - 1)
    kpower = [next(kpowgen) for i in range(n + 1)]
    k1power = [next(k1powgen) for i in range(n + 1)]

    for r in range(1, n + 1):
        f[r][0] = pow(kpower[n] - k1power[n], r, MOD)
    for c in range(1, n + 1):
        f[1][c] = kpower[n - c]

    for r in range(2, n + 1):
        f[r] = [f[r][0]]
        f[r] += [((kpower[n - c] - k1power[n - c]) * k1power[c] * f[r - 1][c]
                  + kpower[n - c] * sum(k1power[c - c0] * nCr[c][c0] * f[r - 1][c - c0] for c0 in range(1, c + 1))) % MOD
                 for c in range(1, n + 1)]
    return f[n][n]


print(main())
