mod = 10 ** 9 + 7
(n, m) = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
xx = [x[i + 1] - x[i] for i in range(n - 1)]
yy = [y[i + 1] - y[i] for i in range(m - 1)]
xsum = sum((xx[i] * (i + 1) * (n - 1 - i) for i in range(n - 1))) % mod
ysum = sum((yy[i] * (i + 1) * (m - 1 - i) for i in range(m - 1))) % mod
print(xsum * ysum % mod)
