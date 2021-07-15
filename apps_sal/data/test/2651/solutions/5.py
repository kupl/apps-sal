n, m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))

area_x = 0
for k in range(n):
    area_x += k * x[k] - (n - k-1) * x[k]

area_y = 0
for l in range(m):
    area_y += l * y[l] - (m - l-1) * y[l]

print(((area_x * area_y) % (10**9 + 7)))

