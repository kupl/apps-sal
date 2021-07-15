n = int(input())
query = [tuple(map(int, input().split())) for _ in range(n)]

x, y = 1, 1
for t, a in query:
    if t >= x and a >= y:
        x = t
        y = a
    else:
        if t < x and a < y:
            x = t * max((x + t - 1) // t, (y + a - 1) // a)
            y = a * max((x + t - 1) // t, (y + a - 1) // a)
        elif t < x:
            x = t * ((x + t - 1) // t)
            y = a * ((x + t - 1) // t)
        else:
            x = t * ((y + a - 1) // a)
            y = a * ((y + a - 1) // a)
print(x + y)
