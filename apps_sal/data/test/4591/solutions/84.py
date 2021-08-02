a, b, c, x, y = list(map(int, input().split()))

c *= 2
t = 0

if a + b > c:
    v = min([x, y])
    t = v * c
    x, y = x - v, y - v

    if x > 0:
        if a < c:
            t = t + a * x
        else:
            t = t + c * x
    elif y > 0:
        if b < c:
            t = t + b * y
        else:
            t = t + c * y
else:
    t = a * x + b * y

print(t)
