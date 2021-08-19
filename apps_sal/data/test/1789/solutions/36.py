(a, b, x, y) = map(int, input().split())
if a < b:
    print(x + min(2 * x, y) * (b - a))
elif a == b:
    print(x)
else:
    print(x + min(2 * x, y) * (a - b - 1))
