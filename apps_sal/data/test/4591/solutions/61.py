(a, b, c, x, y) = map(int, input().split())
print(min(a * x + b * y, max(x, y) * c * 2, min(x, y) * c * 2 + max(0, x - min(x, y)) * a + max(0, y - min(x, y)) * b))
