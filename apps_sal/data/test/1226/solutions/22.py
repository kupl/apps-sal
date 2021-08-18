import sys

N_MAX = 200000 + 5
INF = 10**9 + 7
sys.setrecursionlimit(N_MAX)
MOD = 10**9 + 7

MOD = 10**9 + 7
N_MAX = 2 * 10**5

fac = [1, 1]
facinv = [1, 1]
inv = [0, 1]

for i in range(2, N_MAX + 1):
    fac.append((fac[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    facinv.append((facinv[-1] * inv[-1]) % MOD)


def fac(n, a):
    ans = 1
    for i in range(a):
        ans *= n
        ans %= MOD
        n -= 1
    return ans


def cmb(n, r):
    if (r < 0 or r > n):
        return 0
    return fac[n] * facinv[r] * facinv[n - r] % MOD


def main():
    n, a, b = map(int, sys.stdin.readline().rstrip().split())

    ans = pow(2, n, MOD) - 1
    ans %= MOD

    ans -= fac(n, a) * facinv[a]
    ans %= MOD

    ans -= fac(n, b) * facinv[b]
    ans %= MOD

    print(ans)


main()
