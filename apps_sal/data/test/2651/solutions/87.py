n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

mod = 10 ** 9 + 7
w = 0
for i in range(n - 1):
    w += (x[i + 1] - x[i]) * (i + 1) * (n - i - 1)
    w %= mod
h = 0
for j in range(m - 1):
    h += (y[j + 1] - y[j]) * (j + 1) * (m - j - 1)
    h %= mod
print(h * w % mod)
