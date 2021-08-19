(a, b, c) = map(int, input().split())
data = sorted([(-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a), (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)])
print(data[1])
print(data[0])
