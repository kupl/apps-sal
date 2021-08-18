
x1, y1, x2, y2 = map(int, input().split())

dx = x2 - x1
dy = y2 - y1

#ux = False
#uy = False

# if dx % 2 == 1:
#  ux = True
#  dx += 1

# if dy % 2 == 1:
#  uy = True
#  dy += 1

resx = int(dx / 2 + 1)
resy = int(dy / 2 + 1)

total = resx * resy + (resx - 1) * (resy - 1)

print(total)
return

if ux or uy:
    total -= 1
    if ux:
        total -= dy / 2
    if uy:
        total -= dx / 2

print(int(total))
