import sys

input = sys.stdin.readline
P = 10 ** 9 + 7


def make_fac_tables_mod_p(n, p):
    fac = [0] * (n + 1)
    fac_inv = [0] * (n + 1)
    mod_inv = [0] * (n + 1)
    fac[0] = fac[1] = 1
    fac_inv[0] = fac_inv[1] = 1
    mod_inv[1] = 1
    for i in range(2, n + 1):
        fac[i] = (fac[i - 1] * i) % p
        mod_inv[i] = p - mod_inv[p % i] * (p // i) % p
        fac_inv[i] = fac_inv[i - 1] * mod_inv[i] % p
    return fac, fac_inv


def nCk_mod_p(fac, fac_inv, n, k, p):
    return ((fac[n] * fac_inv[n - k]) % p) * fac_inv[k] % p


def main():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))

    if K == 1:
        print((0))
        return
    if N == 2:
        A.sort()
        print(((A[1] - A[0]) % P))
        return

    A.sort()

    fac, fac_inv = make_fac_tables_mod_p(N - 2, P)

    n_f = N - K + 1
    f = [0] * (n_f + 1)
    k = K - 2
    for i, n in enumerate(list(range(k, N - 2 + 1)), 1):
        f[i] = (f[i - 1] + nCk_mod_p(fac, fac_inv, n, k, P)) % P

    ans = 0
    for i in range(1, n_f + 1):
        ans = (ans - (f[i] * A[n_f - i]) % P) % P

    for i in range(1, n_f + 1):
        ans = (ans + (f[i] * A[N - n_f + i - 1]) % P) % P

    print(ans)


def __starting_point():
    main()

__starting_point()
