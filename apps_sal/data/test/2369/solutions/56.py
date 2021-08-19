def main():
    (n, k) = list(map(int, input().split()))
    a = sorted((int(i) for i in input().split()))
    mod = 10 ** 9 + 7
    comb = [1] * (n - k + 1)
    for i in range(n - k):
        comb[i + 1] = comb[i] * (k + i) * pow(i + 1, mod - 2, mod) % mod
    f = 0
    for i in range(n - k + 1):
        f = (f + a[k + i - 1] * comb[i] % mod) % mod
        f = (f - a[i] * comb[-1 - i] % mod) % mod
    print(f)


def __starting_point():
    main()


__starting_point()
