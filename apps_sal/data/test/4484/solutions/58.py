MOD = 1000000007


def fac(x):
    ret = 1
    for i in range(1, x + 1):
        ret *= i
        ret %= MOD
    return ret


N, M = list(map(int, input().split()))

if N == M:
    print((fac(N)**2 * 2 % MOD))
elif abs(N - M) == 1:
    print((fac(N) * fac(M) % MOD))
else:
    print((0))
