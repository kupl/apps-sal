from functools import lru_cache
L, A, B, mod = list(map(int, input().split()))


def keta(k):
    if A >= 10**k:
        return 0, 0, 0
    begin = 10**(k - 1)
    end = 10**k

    if begin > A + B * (L - 1):
        return 0, 0, 0

    sh = A + max(-1, (begin - 1 - A) // B) * B + B
    ma = min(A + max(0, (end - 1 - A) // B) * B, A + B * (L - 1))
    kou = (ma - sh) // B + 1

    return sh, ma, kou


@lru_cache(maxsize=None)
def f(n, r):
    if n == 1:
        return 1
    if n % 2 == 0:
        return (f(n // 2, r) + pow(r, n // 2, mod) * f(n // 2, r)) % mod
    return (r * f(n - 1, r) + 1) % mod


@lru_cache(maxsize=None)
def g(n, r):
    if n == 1:
        return 0
    if n % 2 == 0:
        return g(n // 2, r) + pow(r, n // 2, mod) * (g(n // 2, r) + n // 2 * f(n // 2, r))
    return r * g(n - 1, r) + r * f(n - 1, r)


keta_count = 1
ANS = 0
for i in range(18, 0, -1):
    sh, ma, kou = keta(i)

    if kou <= 0:
        continue

    ANS = (keta_count * (ma * f(kou, 10**i) - B * g(kou, 10**i)) + ANS) % mod
    keta_count = keta_count * pow(10, kou * i, mod)

print(ANS)
