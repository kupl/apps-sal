(m, b) = map(int, input().split())
mx = 0
for y in range(b, -1, -1):
    x = m * (b - y)
    mx = max(mx, (x + 1) * (y + 1) * (x + y) // 2)
print(mx)
