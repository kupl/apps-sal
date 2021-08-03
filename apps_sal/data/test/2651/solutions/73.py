n, m = list(map(int, input().split()))

x = list(map(int, input().split()))
y = list(map(int, input().split()))

tmp_x = 0
tmp_y = 0
mod = 10**9 + 7
for i, xi in enumerate(x):
    tmp_x += (xi + 1) * (2 * i - (n - 1))

tmp_x = tmp_x % mod

for i, yi in enumerate(y):
    tmp_y += (yi + 1) * (2 * i - (m - 1))

tmp_y = tmp_y % mod

print(((tmp_x * tmp_y) % mod))
