(a, b, x, y) = map(int, input().split())
y = min(y, 2 * x)
if a == b:
    print(x)
elif a > b:
    print(y * (a - b - 1) + x)
elif a < b:
    print(y * (b - a) + x)
