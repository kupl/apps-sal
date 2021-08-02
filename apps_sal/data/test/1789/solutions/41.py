a, b, x, y = list(map(int, input().split()))
now = a

if b < a:
    print((min((a - b - 1) * y + x, x * (a - b - 1) + x * (a - b))))
elif b == a:
    print(x)
else:
    print((min(x + y * (b - a), 2 * x * (b - a) + x)))
