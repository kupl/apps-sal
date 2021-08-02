a, b, c, d = list(map(int, input().split()))


z = (a / b) / (1 - ((1 - (a / b)) * (1 - (c / d))))

print(z)
