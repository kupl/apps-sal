def mingon(angle):
    if angle == 90:
        return 4
    elif angle < 90:
        for i in range(1, 2 * angle + 1):
            if 360 % (2 * angle / i) == 0:
                return int(360 / (2 * angle / i))
    else:
        for i in range(2, 2 * (180 - angle) + 1):
            if 360 % (2 * (180 - angle) / i) == 0:
                return int(360 / (2 * (180 - angle) / i))


t = int(input())
for i in range(t):
    ang = int(input())
    print(mingon(ang))
