def main():
    M = 998244353
    (n, k, *h) = map(int, open(0).read().split())
    m = sum((i != j for (i, j) in zip(h, h[1:] + h[:1])))
    f = [0] * (m + 1)
    f[0] = b = 1
    for i in range(1, m + 1):
        f[i] = b = b * i % M
    inv = [0] * (m + 1)
    inv[m] = b = pow(f[m], M - 2, M)
    for i in range(m, 0, -1):
        inv[i - 1] = b = b * i % M

    def comb(n, k):
        return f[n] * inv[n - k] * inv[k] % M
    print((pow(k, m, M) - sum((comb(m, i) * comb(m - i, i) * pow(k - 2, m - i - i, M) for i in range(m // 2 + 1)))) * pow(k, n - m, M) * pow(2, M - 2, M) % M)


main()
