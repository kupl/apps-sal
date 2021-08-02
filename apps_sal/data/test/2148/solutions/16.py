import math
n, r = map(int, input().split())
v = []
for i in list(map(int, input().split())):
    my = r + 0
    for j in v:
        if j[0] < i and j[0] + r >= i - r or j[0] >= i and j[0] - r <= i + r:
            y = j[1] + math.sqrt(4 * r * r - (j[0] - i)**2)
            if y > my:
                my = y
    v.append((i, my))
for i in v:
    print(i[1], end=' ')
