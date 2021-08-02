mod = 10**9 + 7
h = w = 0
n, m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
for i in range(n - 1):
    h = (h + (x[i + 1] - x[i]) * (n - i - 1) * (i + 1)) % mod
for i in range(m - 1):
    w = (w + (y[i + 1] - y[i]) * (m - i - 1) * (i + 1)) % mod
print((h * w % mod))
