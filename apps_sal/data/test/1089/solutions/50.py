n, m, k = [int(i) for i in input().split()]
mod = 10**9+7


def kai(x, p=mod):
    a = 1
    for i in range(1, x + 1):
        a *= i
        a %= p
    return a


def comb(a, b, p=mod):
    if a < 0 or b < 0:
        return 0
    elif a < b:
        return 0
    c = 1
    c *= kai(a, p)
    c *= pow(kai(b, p), p - 2, p)
    c *= pow(kai(a - b, p), p - 2, p)
    return c % p


ans = 0
for i in range(1, n):
    ans += i * (n - i) * m ** 2
    ans %= mod

for i in range(1, m):
    ans += i * (m - i) * n ** 2
    ans %= mod
ans *= comb(n * m - 2, k - 2)
ans %= mod
print(ans)

