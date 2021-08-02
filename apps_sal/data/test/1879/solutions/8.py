t, sx, sy, ex, ey = [int(x) for x in input().split(' ')]
i = input()

x = ex - sx
y = ey - sy
k = 0
for j in i:
    if y > 0:
        if j == 'N':
            y -= 1
    elif y < 0:
        if j == 'S':
            y += 1

    if x > 0:
        if j == 'E':
            x -= 1
    elif x < 0:
        if j == 'W':
            x += 1

    k += 1
    if x == 0 and y == 0: break

print(k if x == 0 and y == 0 else -1)
