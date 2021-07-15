n, m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))

mod = 10 ** 9 + 7

sx = 0
sy = 0
for i in range(n):
    sx = (sx + x[i] * i - x[i] * (n - 1 - i)) % mod
for i in range(m):
    sy = (sy + y[i] * i - y[i] * (m - 1 - i)) % mod
print((sx * sy % mod))

