def main():
    e = enumerate
    (n, m, *u) = map(int, open(0).read().split())
    dp = [[1] * (m + 1) for _ in range(n + 1)]
    dpi = dp[0]
    for (i, s) in e(u[:n]):
        dpi1 = dp[i + 1]
        for (j, t) in e(u[n:]):
            dpi1[j + 1] = (dpi[j + 1] + dpi1[j] - dpi[j] * (s != t)) % (10 ** 9 + 7)
        dpi = dpi1
    print(dpi[m])


main()
