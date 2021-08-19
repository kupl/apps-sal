(x1, y1) = map(int, input().split())
(x2, y2) = map(int, input().split())
(x3, y3) = map(int, input().split())


def mirror(x1, y1, x2, y2, x3, y3):
    x_mid = (x1 + x2) / 2
    if x3 < x_mid:
        x3 += 2 * (x_mid - x3)
    else:
        x3 -= 2 * (x3 - x_mid)
    y_mid = (y1 + y2) / 2
    if y3 < y_mid:
        y3 += 2 * (y_mid - y3)
    else:
        y3 -= 2 * (y3 - y_mid)
    return (x3, y3)


answer = []
(x, y) = mirror(x1, y1, x2, y2, x3, y3)
if int(x) == x and int(y) == y:
    answer.append([x, y])
(x, y) = mirror(x1, y1, x3, y3, x2, y2)
if int(x) == x and int(y) == y:
    answer.append([x, y])
(x, y) = mirror(x3, y3, x2, y2, x1, y1)
if int(x) == x and int(y) == y:
    answer.append([x, y])
print(len(answer))
for i in answer:
    print(int(i[0]), int(i[1]))
