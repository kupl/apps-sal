(n, m) = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
mod = 10 ** 9 + 7
sum_x = 0
sum_y = 0
for i in range(n):
    sum_x += i * x[i] - (n - i - 1) * x[i]
for i in range(m):
    sum_y += i * y[i] - (m - i - 1) * y[i]
print(sum_x * sum_y % mod)
