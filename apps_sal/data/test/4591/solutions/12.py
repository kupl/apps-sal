(a, b, c, x, y) = map(int, input().split())
if x > y:
    cost = min(x * a + y * b, max(x, y) * 2 * c, y * 2 * c + (x - y) * a)
else:
    cost = min(x * a + y * b, max(x, y) * 2 * c, x * 2 * c + (y - x) * b)
print(cost)
