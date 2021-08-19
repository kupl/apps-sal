n, m, k = list(map(int, input().split()))

mod = 10**9 + 7

# (n * m - 2)C(k - 2)
# 距離xの組 -  n - x + 1
# 横 n - x + 1
# 縦 m * m
ans = 0
for y in range(1, n):
    ans += y * (n - y) * m * m % mod
for x in range(1, m):
    ans += x * (m - x) * n * n % mod


def inv(x):
    return pow(x, mod - 2, mod)


# comb
for i in range(k - 2):
    ans = ans * (n * m - 2 - i) * inv(i + 1) % mod

print(ans)
