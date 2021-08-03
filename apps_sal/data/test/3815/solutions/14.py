import sys


MOD = 10**9 + 9


def inv(x):
    return pow(x, MOD - 2, MOD)


def alternateSum(n, a, b, k, s):
    res = 0
    q = (pow(b, k, MOD) * inv(pow(a, k, MOD))) % MOD
    max_pow = pow(a, n, MOD)
    c = b * inv(a) % MOD
    for i in range(k):
        if s[i] == '+':
            res += max_pow
        elif s[i] == '-':
            res -= max_pow
        res %= MOD
        max_pow = (max_pow * c) % MOD
    t = (n + 1) // k
    if q == 1:
        return (t * res) % MOD
    z = ((pow(q, t, MOD) - 1) * inv(q - 1)) % MOD
    return z * res % MOD


n, a, b, k, s = sys.stdin.read().split()
result = alternateSum(int(n), int(a), int(b), int(k), s)

print(result)
