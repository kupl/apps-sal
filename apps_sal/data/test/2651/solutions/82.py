mod = 10 ** 9 + 7

n, m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))

sum_x = 0
for i in range(1, n + 1):
    sum_x += (i - 1) * x[i - 1] - (n - i) * x[i - 1]

sum_y = 0
for i in range(1, m + 1):
    sum_y += (i - 1) * y[i - 1] - (m - i) * y[i - 1]

print((sum_x * sum_y % mod))

