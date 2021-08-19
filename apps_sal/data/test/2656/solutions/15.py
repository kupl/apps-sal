import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
MAX = 2 * 10 ** 6 + 10
MOD = 10 ** 9 + 7
fac = [1] * MAX
f_inv = [1] * MAX


def prepare(n, mod):
    for i in range(1, n + 1):
        fac[i] = fac[i - 1] * i % mod
    f_inv[n] = pow(fac[n], -1, MOD)
    for i in range(n - 1, 0, -1):
        f_inv[i] = f_inv[i + 1] * (i + 1) % MOD


def modcmb(n, r, mod):
    if n < 0 or r < 0:
        return 0
    if r > n:
        return 0
    return fac[n] * f_inv[r] * f_inv[n - r] % mod


def main():
    K = int(readline())
    S = readline().strip()
    N = len(S)
    prepare(N + K + 5, MOD)
    inv26 = pow(26, -1, MOD)
    pow26 = pow(26, K, MOD)
    pow25 = 1
    ans = 0
    for i in range(K + 1):
        ans += modcmb(N - 1 + i, i, MOD) * pow25 * pow26 % MOD
        ans %= MOD
        pow25 *= 25
        pow25 %= MOD
        pow26 *= inv26
        pow26 %= MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
