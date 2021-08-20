(a, b, x, y) = map(int, input().split())
if a > b:
    print((a - b - 1) * min(2 * x, y) + x)
else:
    print((b - a) * min(2 * x, y) + x)
