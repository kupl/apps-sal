(n, m) = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
sum_x = 0
sum_y = 0
for i in range(n):
    sum_x += x[i] * i
    sum_x -= x[i] * (n - 1 - i)
for i in range(m):
    sum_y += y[i] * i
    sum_y -= y[i] * (m - 1 - i)
mod = 10 ** 9 + 7
print(sum_x % mod * (sum_y % mod) % mod)
