(a, b, f, k) = map(int, input().split())
x = 0
g = b
for kk in range(k - 1):
    if kk % 2 == 0:
        d = a + (a - f)
        if g < d:
            if g < f:
                x = -1
                break
            x += 1
            g = b - (a - f)
            if g < 0:
                x = -1
                break
        else:
            g -= a
    else:
        d = a + f
        if g < d:
            if g < a - f:
                x = -1
                break
            x += 1
            g = b - f
            if g < 0:
                x = -1
                break
        else:
            g -= a
if (k - 1) % 2 == 0:
    if g < a:
        if g < f:
            x = -1
        else:
            x += 1
            g = b - (a - f)
            if g < 0:
                x = -1
elif g < a:
    if g < a - f:
        x = -1
    else:
        x += 1
        g = b - f
        if g < 0:
            x = -1
print(x)
