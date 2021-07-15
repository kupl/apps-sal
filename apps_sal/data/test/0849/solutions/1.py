a, b, c, d = list(map(int, input().split()))
p1 = a / b
p2 = c / d
print(p1 / (1 - (1 - p1) * (1 - p2)))

