n, m = map(int, input().split())
mod = 10**9 + 7

x = sorted(list(map(int, input().split())))
y = sorted(list(map(int, input().split())))

X = 0
for i in range(n - 1):
    X += (i + 1) * (n - i - 1) * (x[i + 1] - x[i]) % mod
    X %= mod

Y = 0
for i in range(m - 1):
    Y += (i + 1) * (m - i - 1) * (y[i + 1] - y[i]) % mod
    Y %= mod

print(X * Y % mod)
