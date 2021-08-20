(n, a, b) = map(int, input().split())
mod = 10 ** 9 + 7
ans = pow(2, n, mod) - 1
a = min(a, n - a)
b = min(b, n - b)
c = min(a, b)
(x, y) = (1, 1)
for i in range(1, c + 1):
    x = x * (n + 1 - i) % mod
    y = y * i % mod
ans -= x * pow(y, mod - 2, mod) % mod
for i in range(c + 1, max(a, b) + 1):
    x = x * (n + 1 - i) % mod
    y = y * i % mod
ans -= x * pow(y, mod - 2, mod) % mod
print(ans % mod)
