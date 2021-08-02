a, b, c, d = map(int, input().split())
q = (1 - a / b) * (1 - c / d)
print(a / b / (1 - q))
