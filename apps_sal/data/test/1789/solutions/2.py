(a, b, x, y) = list(map(int, input().split()))
print(abs((b - a) * 2 + 1) // 2 * min(x * 2, y) + x)
