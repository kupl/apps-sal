(x1, y1, x2, y2) = input().split()
(dx, dy) = (int(x2) - int(x1), int(y2) - int(y1))
if dy % 2 != 0:
    print(dy + 1) // 2 * (dx + 1)
else:
    print((dy // 2 + 1) * (dx // 2 + 1) + dy // 2 * dx // 2)
