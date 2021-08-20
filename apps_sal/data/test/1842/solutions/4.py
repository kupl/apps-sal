(a, b, c) = list(map(int, input().split()))
d = (b * b - 4 * a * c) ** 0.5
print(max((-b + d) / (2 * a), (-b - d) / (2 * a)))
print(min((-b + d) / (2 * a), (-b - d) / (2 * a)))
