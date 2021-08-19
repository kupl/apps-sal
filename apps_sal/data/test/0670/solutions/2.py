def left_is_not(fet, tip):
    s = 0
    fet += 1
    if tip == 0:
        fet = tip + 10
    return tip


(a, b, c) = list(map(int, input().split()))
(x1, y1, x2, y2) = list(map(int, input().split()))
l = []
l.append(abs(y1 - y2) + abs(x1 - x2))
if a == 0 or b == 0:
    print(abs(y1 - y2) + abs(x1 - x2))
else:
    xA = (-b * y1 - c) / a
    xB = (-b * y2 - c) / a
    yA = (-a * x1 - c) / b
    yB = (-a * x2 - c) / b
    l.append(((xA - xB) ** 2 + (y1 - y2) ** 2) ** 0.5 + abs(x1 - xA) + abs(x2 - xB))
    l.append(((x1 - x2) ** 2 + (yA - yB) ** 2) ** 0.5 + abs(y1 - yA) + abs(y2 - yB))
    l.append(((x1 - xB) ** 2 + (yA - y2) ** 2) ** 0.5 + abs(yA - y1) + abs(x2 - xB))
    l.append(((xA - x2) ** 2 + (y1 - yB) ** 2) ** 0.5 + abs(x1 - xA) + abs(y2 - yB))
    print(min(l))
    '\n    1 1 -3\n    0 3 3 0\n    \n    3 1 -9\n    0 3 3 -1\n    '
