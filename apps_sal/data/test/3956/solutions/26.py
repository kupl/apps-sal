from collections import Counter
K, N = map(int, input().split())
mod = 998244353
frac = [1] * 5010
for i in range(2, 5010):
    frac[i] = i * frac[i - 1] % mod
fraci = [None] * 5010
for i in range(5010):
    fraci[i] = pow(frac[i], mod - 2, mod)


def comb(a, b):
    if not a >= b >= 0:
        return 0
    return frac[a] * fraci[b] * fraci[a - b] % mod


A = Counter()


def calc(x):
    if A[x]:
        return A[x]
    res = 0
    for i in range(N // 2 + 1):
        res = (res + (-1)**i * comb(x, i) * comb(N + K - 1 - 2 * i, N - 2 * i)) % mod
    A[x] = res
    return res


for j in range(2, 2 * K + 1):
    print(calc(min(j, (2 * K + 2 - j)) // 2))
