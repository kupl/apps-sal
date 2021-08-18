from math import sqrt

p, y = list(map(int, input().split()))

yp = int(sqrt(y))

if yp > p:
    yp = p
    if yp % 2 == 0:
        yp -= 1

if p == 2:
    if y == 2:
        print(-1)
        return
    if y % 2 == 0:
        print(y - 1)
        return
    else:
        print(y)
        return


if yp % 2 == 0:
    yp -= 1

if y % 2 == 0:
    y -= 1


if yp == 1:
    if y > 2 and y % 2 == 0:
        print(y - 1)
        return
    if y > p:
        print(y)
        return
    else:
        print(-1)
        return

while y > p:
    yr = yp
    while yr > 2:
        if y % yr == 0:
            yr -= 2
            break

        elif yr == 3:
            print(y)
            return

        elif yr > 3:
            yr -= 2

    y -= 2

print("-1")
