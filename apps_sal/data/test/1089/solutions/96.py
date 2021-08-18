
def LI():
    return list(map(int, input().split()))


N, M, K = LI()

MOD = 10 ** 9 + 7
MAX = 10 ** 5 * 2
fac, finv, inv = [None] * MAX, [None] * MAX, [None] * MAX


def comb_init():
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = -inv[MOD % i] * int(MOD / i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD


def comb(n, k):
    if n < k or n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


def s(x):
    return x * (x + 1) // 2


def cal(a, b):
    ret = a * s(b - 1) + b * s(a - 1)
    return ret % MOD


def main():
    comb_init()
    ans = 0
    for i in range(N):
        for j in range(M):
            v = cal(N - i, M - j) + cal(N - i, j + 1) - (s(j) + s(N - i - 1))
            ans = (ans + v) % MOD

    ans = ans * comb(N * M - 2, K - 2) % MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
