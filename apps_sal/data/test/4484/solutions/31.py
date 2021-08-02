mod = 10**9 + 7
n, m = map(int, input().split())
if abs(n - m) >= 2:
    print(0)
    return
x, y = 1, 1
for i in range(1, n + 1):
    x *= i
    x %= mod
for i in range(1, m + 1):
    y *= i
    y %= mod
if n == m:
    print((2 * x * y) % mod)
else:
    print((x * y) % mod)
