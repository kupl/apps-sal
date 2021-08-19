(n, m) = map(int, input().split())
MOD = 1000000007
x = list(map(int, input().split()))
y = list(map(int, input().split()))
sx = 0
sy = 0
for i in range(1, n):
    sx += (x[i] - x[i - 1]) * i * (n - i)
    sx %= MOD
for i in range(1, m):
    sy += (y[i] - y[i - 1]) * i * (m - i)
    sy %= MOD
print(sx * sy % MOD)
