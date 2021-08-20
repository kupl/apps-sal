import math


def __starting_point():
    (x, y) = (int(a) for a in input().split(' '))
    ans = []
    if x == 0:
        ans.append((0, 1))
        ans.append((0, y))
        ans.append((0, 0))
        ans.append((0, y - 1))
    elif y == 0:
        ans.append((1, 0))
        ans.append((x, 0))
        ans.append((0, 0))
        ans.append((x - 1, 0))
    elif x > y:
        if y < 2 or math.sqrt(x ** 2 + y ** 2) + x > 2 * math.sqrt(x ** 2 + (y - 1) ** 2):
            ans.append((0, 0))
            ans.append((x, y))
            ans.append((0, y))
            ans.append((x, 0))
        else:
            ans.append((0, 1))
            ans.append((x, y))
            ans.append((0, 0))
            ans.append((x, y - 1))
    elif x < 2 or math.sqrt(x ** 2 + y ** 2) + y > math.sqrt(y ** 2 + (x - 1) ** 2) + math.sqrt(y ** 2 + (x - 1) ** 2):
        ans.append((0, 0))
        ans.append((x, y))
        ans.append((x, 0))
        ans.append((0, y))
    else:
        ans.append((1, 0))
        ans.append((x, y))
        ans.append((0, 0))
        ans.append((x - 1, y))
    for a in ans:
        print(str(a[0]) + ' ' + str(a[1]))


__starting_point()
