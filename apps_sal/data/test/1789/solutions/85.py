a, b, x, y = list(map(int, input().split()))
d = abs(2 * b + 1 - 2 * a)
print(((d // 2) * min(2 * x, y) + x))
