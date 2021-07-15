x, y = map(int, input().split())
z = []
print((6 * x - 1) * y)
for i in range(0, x):
    z.append((6 * i + 1) * y); z.append((6 * i + 3) * y); z.append((6 * i + 4) * y); z.append((6 * i + 5) * y)
    print(*z)
    z.clear()
