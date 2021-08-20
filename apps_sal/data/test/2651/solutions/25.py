(n, m) = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
mod = 10 ** 9 + 7
(vx, vy) = (0, 0)
for i in range(n - 1):
    vx += (x[i + 1] - x[i]) * (i + 1) * (n - i - 1)
    vx %= mod
for i in range(m - 1):
    vy += (y[i + 1] - y[i]) * (i + 1) * (m - i - 1)
    vy %= mod
print(vx * vy % mod)
