def comb(n, r, m):
    if 2 * r > n:
        r = n - r
    nume, deno = 1, 1
    for i in range(1, r + 1):
        nume *= (n - i + 1)
        nume %= m
        deno *= i
        deno %= m

    return (nume * pow(deno, m - 2, m)) % m


def main():
    N, M, K = list(map(int, input().split()))
    mod = 998244353

    ans, comb_r = pow(M - 1, N - 1, mod), 1
    for r in range(1, K + 1):
        comb_r = (comb_r * (N - r) * pow(r, mod - 2, mod)) % mod
        ans = (ans + comb_r * pow(M - 1, N - r - 1, mod)) % mod
    ans = (ans * M) % mod

    print(ans)


def __starting_point():
    main()


__starting_point()
