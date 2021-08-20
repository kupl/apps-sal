(n, m) = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
mod = 10 ** 9 + 7
sx = 0
for i in range(n - 1):
    xi = (x[i + 1] - x[i]) % mod
    sx += (i + 1) * (n - i - 1) * xi % mod
    sx %= mod
sy = 0
for i in range(m - 1):
    yi = (y[i + 1] - y[i]) % mod
    sy += (i + 1) * (m - i - 1) * yi % mod
    sy %= mod
print(sx * sy % mod)
