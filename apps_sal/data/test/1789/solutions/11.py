a, b, x, y = list(map(int, input().split()))
if a > b:
    print((x + abs(a - b - 1) * min(2 * x, y)))
elif a < b:
    print((x + abs(a - b) * min(2 * x, y)))
elif a == b:
    print(x)
