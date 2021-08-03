n, m = map(int, input().split())
n, m = n - 1, m - 1
x = list(map(int, input().split()))
y = list(map(int, input().split()))
mod = 10 ** 9 + 7
x.sort()
y.sort()

h, w = 0, 0
for i in range(n):
    h += (i + 1) * (n - i) * (x[i + 1] - x[i])
    h %= mod

for j in range(m):
    w += (j + 1) * (m - j) * (y[j + 1] - y[j])
    w %= mod

print(h * w % mod)
