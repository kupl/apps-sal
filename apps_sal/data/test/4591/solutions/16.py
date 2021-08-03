a, b, c, x, y = map(int, input().split())
if a + b <= 2 * c:
    print(a * x + b * y)
else:
    print(c * 2 * min(x, y) + min(max(a * (x - y), b * (y - x)), c * 2 * abs(x - y)))
