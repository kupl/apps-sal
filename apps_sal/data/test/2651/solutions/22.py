MOD = 1000000007
n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
xs = ys = 0
for i in range(1, n + 1):
    xs += ((i - 1) * x[i - 1] - (n - i) * x[i - 1])
    xs %= MOD
for i in range(1, m + 1):
    ys += ((i - 1) * y[i - 1] - (m - i) * y[i - 1])
    ys %= MOD
ans = xs * ys
print(ans % MOD)
