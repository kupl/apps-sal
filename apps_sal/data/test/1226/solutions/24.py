(n, a, b) = map(int, input().split())
mod = 10 ** 9 + 7
ans = pow(2, n, mod) - 1
(x, y) = (1, 1)
for i in range(a):
    x *= n - i
    y *= i + 1
    (x, y) = (x % mod, y % mod)
ans -= x * pow(y, mod - 2, mod) % mod
(x, y) = (1, 1)
for i in range(b):
    x *= n - i
    y *= i + 1
    (x, y) = (x % mod, y % mod)
ans -= x * pow(y, mod - 2, mod) % mod
print(ans % mod)
