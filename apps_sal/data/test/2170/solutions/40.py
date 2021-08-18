import sys

MOD = 10**9 + 7
N_MAX = 5 * 10**5

fac = [1, 1]
facinv = [1, 1]
inv = [0, 1]

for i in range(2, N_MAX + 1):
    fac.append((fac[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    facinv.append((facinv[-1] * inv[-1]) % MOD)


def cmb(n, r):
    if (r < 0 or r > n):
        return 0
    return fac[n] * facinv[r] * facinv[n - r] % MOD


def prm(n, r):
    if (r < 0 or r > n):
        return 0
    return fac[n] * facinv[n - r] % MOD


def main():
    N, M = list(map(int, sys.stdin.readline().rstrip().split()))

    all = prm(M, N) ** 2 % MOD

    dup = 0

    for i in range(1, N + 1):

        tmp = prm(M, i) * prm(M - i, N - i) ** 2 % MOD
        tmp *= cmb(N, i) * (-1) ** (i - 1)

        dup += tmp % MOD

    print(((all - dup) % MOD))


main()
