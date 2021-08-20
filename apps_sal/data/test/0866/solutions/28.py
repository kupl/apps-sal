(X, Y) = map(int, input().split())
MOD = 10 ** 9 + 7


def modpow(x, n):
    ret = 1
    while n > 0:
        if n & 1:
            ret = ret * x % MOD
        x = x * x % MOD
        n >>= 1
    return ret


def modinv(x):
    return modpow(x, MOD - 2)


def modf(x):
    ret = 1
    for i in range(2, x + 1):
        ret *= i
        ret %= MOD
    return ret


ans = 0
if (X + Y) % 3 == 0:
    m = (2 * X - Y) // 3
    n = (2 * Y - X) // 3
    if m >= 0 and n >= 0:
        ans = modf(m + n) * modinv(modf(n) * modf(m))
        ans %= MOD
print(ans)
