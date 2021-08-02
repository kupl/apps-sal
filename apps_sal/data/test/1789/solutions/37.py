a, b, x, y = list(map(int, input().split()))
z = min(2 * x, y)
if a <= b:
    print((x + z * (b - a)))
else:
    print((x + z * (a - b - 1)))
