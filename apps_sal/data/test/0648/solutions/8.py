def I(): return list(map(int, input().split()))


m, b = I()
mx = 0
for y in range(0, 100001):
    x = m * (b - y)
    if x >= 0:
        mx = max(mx, (y + 1) * x * (x + 1) // 2 + (x + 1) * y * (y + 1) // 2)
print(mx)
