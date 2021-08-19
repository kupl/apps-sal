mod = 10 ** 9 + 7


def comb(n, r):
    r = min(r, n - r)
    a = b = 1
    for _ in range(r):
        a *= n
        b *= r
        a %= mod
        b %= mod
        n -= 1
        r -= 1
    return a * pow(b, mod - 2, mod) % mod


S = int(input())
ans = 0
n = 1
while 3 * n <= S:
    r = S - 3 * n
    ans += comb(n + r - 1, r)
    ans %= mod
    n += 1
print(ans)
