a, b, c = list(map(int, input().split()))
D = b * b - 4 * a * c
x = (-b + D ** 0.5) / 2 / a
y = (-b - D ** 0.5) / 2 / a
print(max(x, y))
print(min(x, y))

