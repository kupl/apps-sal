(n, m) = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
MOD = 10 ** 9 + 7
xx = [x[i + 1] - x[i] for i in range(n - 1)]
yy = [y[i + 1] - y[i] for i in range(m - 1)]
print(sum((xx[i] * (i + 1) * (n - 1 - i) for i in range(n - 1))) * sum((yy[i] * (i + 1) * (m - 1 - i) for i in range(m - 1))) % MOD)
