n = int(input())

mod = 10**9 + 7

a = [0] * n
c = [0] * n
g = [0] * n
t = [0] * n

a[0] = c[0] = g[0] = t[0] = 1
a[1] = c[1] = g[1] = t[1] = 4
a[2], c[2], g[2], t[2] = 16, 14, 15, 16

for i in range(3, n):
    v = (a[i - 1] + c[i - 1] + g[i - 1] + t[i - 1]) % mod
    a[i] = v
    c[i] = (v - a[i - 2] - g[i - 2] - 3 * a[i - 3]) % mod
    g[i] = (v - a[i - 2] + g[i - 3]) % mod
    t[i] = v
print((a[n - 1] + c[n - 1] + g[n - 1] + t[n - 1]) % mod)
