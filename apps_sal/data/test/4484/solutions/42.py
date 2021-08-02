MOD = pow(10, 9) + 7


def MODINV(n: int, MOD=MOD):
    return pow(n, MOD - 2, MOD)


def perm(n, k, MOD):
    numer = 1
    for i in range(n, n - k, -1):
        numer *= i
        numer %= MOD
    return numer


def main():
    N, M = list(map(int, input().split()))
    if N == M + 1 or N + 1 == M:
        ans = (perm(N, N, MOD) * perm(M, M, MOD)) % MOD
    elif N == M:
        ans = (2 * (perm(N, N, MOD) * perm(M, M, MOD))) % MOD
    else:
        ans = 0
    print(ans)


def __starting_point():
    main()


__starting_point()
