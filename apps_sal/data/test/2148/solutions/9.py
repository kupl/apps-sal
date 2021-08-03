n, r = list(map(int, input().split()))
x = list(map(int, input().split()))

r2r4 = 4 * r**2

y = []
for i in range(0, n):
    max_y = r
    for j in range(i):
        if r2r4 >= (x[i] - x[j]) ** 2:
            max_y = max(max_y, y[j] + (r2r4 - (x[i] - x[j])**2)**0.5)
    y.append(max_y)

print(*y)
