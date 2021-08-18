a, b, x, y = list(map(int, input().split()))
if a == b:
    print(x)
if a < b:
    dif = b - a
    print((min(
        dif * y + x,
        dif * 2 * x + x)))
if a > b:
    dif = a - b
    print((min(
        (2 * dif - 1) * x,
        (dif - 1) * y + x
    )))
