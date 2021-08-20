(a, b, c, x, y) = map(int, input().split())
result = []
if x > y:
    result.append(a * x + b * y)
    result.append(a * (x - y) + 2 * c * y)
    result.append(2 * c * x)
elif x < y:
    result.append(a * x + b * y)
    result.append(b * (y - x) + 2 * c * x)
    result.append(2 * c * y)
else:
    result.append(a * x + b * y)
    result.append(2 * c * x)
print(min(result))
