(a, b, c, x, y) = map(int, input().split())
ab = a * x + b * y
cc = c * 2 * max(x, y)
abcc = c * 2 * min(x, y) + (b if x < y else a) * abs(x - y)
print(min(ab, cc, abcc))
