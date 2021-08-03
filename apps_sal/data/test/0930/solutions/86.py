import sys
input = sys.stdin.readline


def read():
    N, K = list(map(int, input().strip().split()))
    return N, K


def binom_preprocess(n, MOD=10**9 + 7):
    f = [0 for i in range(n + 1)]  # n!
    invf = [0 for i in range(n + 1)]  # (n!)^-1
    f[0] = 1
    f[1] = 1
    invf[0] = 1
    invf[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] * i % MOD
    invf[n] = pow(f[n], MOD - 2, MOD)
    for i in range(n, 2, -1):
        invf[i - 1] = invf[i] * i % MOD
    return f, invf


def binom(n, k, f, invf, MOD=10**9 + 7):
    if n < k or n < 0 or k < 0:
        return 0
    else:
        return (f[n] * invf[k] % MOD) * invf[n - k] % MOD


def solve(N, K, MOD=10**9 + 7):
    # k: 人数0の部屋の数
    # N人を(N-k)部屋に押し込む方法を考える
    f, invf = binom_preprocess(N, MOD)
    ans = 0
    for k in range(0, min(N, K + 1)):
        ans += binom(N, k, f, invf, MOD) * binom(N - 1, k, f, invf, MOD)
        ans %= MOD
    return ans


def __starting_point():
    inputs = read()
    print(("{}".format(solve(*inputs))))


__starting_point()
