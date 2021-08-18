def sign(x):
    return 1 if x > 0 else -1


def dis(x):
    if x >= 360:
        x %= 360

    if x <= -180:
        return 360 + x
    elif x <= 0:
        return abs(x)
    elif x <= 180:
        return x
    else:
        return 360 - x


def __starting_point():

    x = int(input())
    x = (-sign(x)) * (abs(x) % 360)

    mindis = dis(x)
    res = 0

    for i in range(1, 4):
        newdis = dis(x + 90 * i)
        if newdis < mindis:
            mindis = newdis
            res = i

    print(res)


__starting_point()
