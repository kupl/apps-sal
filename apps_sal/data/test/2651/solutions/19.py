n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

mod = 10**9 + 7

sidex, sidey = 0, 0

for i in range(1, n):
    sidex += (x[i] - x[i - 1]) * i * (n - i) % mod

for i in range(1, m):
    sidey += (y[i] - y[i - 1]) * i * (m - i) % mod

print(sidex * sidey % mod)
