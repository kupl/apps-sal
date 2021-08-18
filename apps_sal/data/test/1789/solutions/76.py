a, b, x, y = list(map(int, input().split()))

if b < a:
    d1 = abs(b + 1 - a) * y + x
    d2 = (abs(b - a) * 2 - 1) * x
else:
    d1 = abs(b - a) * y + x
    d2 = (abs(b - a) * 2 + 1) * x
print((min(d1, d2)))
