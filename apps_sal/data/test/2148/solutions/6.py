from math import sqrt
s = str(input())
(n, r) = (int(s.split(' ')[0]), float(s.split(' ')[1]))
xs = str(input()).split(' ')
xs = [int(x) for x in xs]
locations = []
for x in xs:
    y = r
    for loc in locations:
        (x2, y2) = loc
        if abs(x2 - x) <= 2 * r:
            y = max(y, y2 + sqrt(4 * r * r - abs(x2 - x) * abs(x2 - x)))
    locations.append((x, y))
for l in locations:
    print(str(l[1]), end=' ')
