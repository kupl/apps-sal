n, m, k = list(map(int, input().split()))

mod = 10**9 + 7

ans = 0
for y in range(1, n):
    ans += y * (n - y) * m * m % mod
for x in range(1, m):
    ans += x * (m - x) * n * n % mod


def inv(x):
    return pow(x, mod - 2, mod)


for i in range(k - 2):
    ans = ans * (n * m - 2 - i) * inv(i + 1) % mod

print(ans)
