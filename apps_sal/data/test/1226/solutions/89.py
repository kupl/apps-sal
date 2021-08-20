def main():
    import sys

    def input():
        return sys.stdin.readline().strip()
    (N, A, B) = map(int, input().split())
    mod = 10 ** 9 + 7

    def modinv(a, mod=10 ** 9 + 7):
        return pow(a, mod - 2, mod)

    def cmb(n, r, mod=10 ** 9 + 7):
        r = min(r, n - r)
        res = 1
        for i in range(r):
            res = res * (n - i) * modinv(i + 1, mod) % mod
        return res
    ans = pow(2, N, mod) - 1 - cmb(N, A, mod) - cmb(N, B, mod)
    print(ans % mod)


def __starting_point():
    main()


__starting_point()
