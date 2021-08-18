n, m = map(int, input().split())
if n + m == 2:
    print(2)
    return
if n > m:
    n, m = m, n
a, b, c, d = 1, 1, 1, 1
mod = 10 ** 9 + 7
for i in range(2, m):
    a, b, c, d = c, a + c, b + d, b
    a %= mod
    b %= mod
    c %= mod
    d %= mod
if n == 1:
    print((a + b + c + d) % mod)
    return
a1 = b1 = c1 = d1 = 1
for i in range(2, n):
    a1, b1, c1, d1 = c1, a1 + c1, b1 + d1, b1
    a1 %= mod
    b1 %= mod
    c1 %= mod
    d1 %= mod
print((a + b + c + d + a1 + b1 + c1 + d1 - 2 + mod) % mod)
