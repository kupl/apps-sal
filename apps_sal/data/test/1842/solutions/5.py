(a, b, c) = list(map(int, input().split()))
d = b ** 2 - 4 * a * c
x1 = (-b + d ** 0.5) / (2 * a)
x2 = (-b - d ** 0.5) / (2 * a)
(x1, x2) = (min(x1, x2), max(x1, x2))
print(x2)
print(x1)
