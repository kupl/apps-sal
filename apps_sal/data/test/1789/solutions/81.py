a, b, x, y = map(int, input().split())
z = min(x * 2, y)
d = abs(b * 2 - a * 2 + 1) // 2
print(d * z + x)
