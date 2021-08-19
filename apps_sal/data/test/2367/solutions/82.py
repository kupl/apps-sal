(h, w, a, b) = list(map(int, input().split()))
MOD = 1000000007


def modPow(a, x, p):
    res = 1
    while x > 0:
        if x % 2 != 0:
            res = res * a % p
        a = a * a % p
        x /= 2
    return res


fact = [None] * 220000
for i in range(1, 220000):
    fact[0] = 1
    fact[i] = i * fact[i - 1] % MOD


def ncr(n, r):
    den = fact[n - r] * fact[r] % MOD
    return fact[n] * pow(den, MOD - 2, MOD) % MOD


def number_of_paths(h, w):
    n = h + w - 2
    r = h - 1
    return ncr(n, r)


ans = 0
for i in range(b + 1, w + 1):
    ans += number_of_paths(h - a, i) * number_of_paths(a, w - i + 1)
print(int(ans % MOD))
