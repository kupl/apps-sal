a, b, x, y = map(int, input().split())
if a <= b:
    print(min(x + y * (b - a), x * ((b - a) * 2 + 1)))
else:
    print(min(x + y * (a - b - 1), x * ((a - b) * 2 - 1)))
