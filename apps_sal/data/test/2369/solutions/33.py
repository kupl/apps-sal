import sys
MOD = 10 ** 9 + 7
N_MAX = 10 ** 5 + 1
fac = [1, 1]
facinv = [1, 1]
inv = [0, 1]
for i in range(2, N_MAX + 1):
    fac.append(fac[-1] * i % MOD)
    inv.append(-inv[MOD % i] * (MOD // i) % MOD)
    facinv.append(facinv[-1] * inv[-1] % MOD)


def cmb(n, r):
    if r < 0 or r > n:
        return 0
    return fac[n] * facinv[r] * facinv[n - r] % MOD


def main():
    (N, K) = list(map(int, sys.stdin.readline().rstrip().split()))
    A = [int(x) for x in sys.stdin.readline().rstrip().split()]
    A.sort()
    sum = 0
    for i in range(N - K + 1):
        sum += cmb(N - i - 1, K - 1) * (A[-(i + 1)] - A[i]) % MOD
        sum %= MOD
    print(sum)


main()
