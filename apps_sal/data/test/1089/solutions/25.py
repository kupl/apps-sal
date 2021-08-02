def cmb(a, b, c):
    b = min(b, a - b)
    num = 1
    for i in range(b):
        num = num * (a - i) % c
    den = 1
    for i in range(b):
        den = den * (i + 1) % c
    return num * pow(den, c - 2, c) % c


n, m, k = list(map(int, input().split()))
mod = 10**9 + 7
ans = 0
C = cmb(n * m - 2, k - 2, mod)
for i in range(1, n):
    ans += i * (n - i) * m**2 * C
    ans %= mod
for i in range(1, m):
    ans += i * (m - i) * n**2 * C
    ans %= mod
print(ans)
