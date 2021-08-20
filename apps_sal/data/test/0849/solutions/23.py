(a, b, c, d) = map(float, input().split())
t = (1 - a / b) * (1 - c / d)
print(a / b / (1 - t))
