def main():
    import sys
    input = sys.stdin.readline
    '"ここに今までのコード'
    (n, k) = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    ans = 0
    baig = [0 for i in range(10 ** 5 + 1)]
    for i in range(1, k + 1):
        baig[i] = pow(k // i, n, MOD)
    for j in range(k, 0, -1):
        for jj in range(2 * j, k + 1, j):
            baig[j] -= baig[jj]
        baig[j] %= MOD
        ans += baig[j] * j
        ans %= MOD
    print(int(ans))


def __starting_point():
    main()


__starting_point()
