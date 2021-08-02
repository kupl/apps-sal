a, b, c, x, y = map(int, input().split())
if x > y:
    cost = min(a * x + b * y, x * c * 2, y * c * 2 + (x - y) * a)
else:
    cost = min(a * x + b * y, y * c * 2, x * c * 2 + (y - x) * b)

print(cost)
