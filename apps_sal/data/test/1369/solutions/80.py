n = int(input())
C = []
for i in range(n):
    x, y = list(map(int, input().split()))
    C.append(complex(x, y))


def calc_kyori(O, C):
    res = 0
    for i in range(n):
        temp = abs(O - C[i])
        res = max(temp, res)
    return res


def sannbunn_first(x, my, MY):
    cnt = 100
    while cnt > 0:
        y1 = (2 * my + MY) / 3
        y2 = (my + 2 * MY) / 3
        v1 = calc_kyori(complex(x, y1), C)
        v2 = calc_kyori(complex(x, y2), C)
        if v2 < v1:
            my = y1
        else:
            MY = y2
        cnt -= 1
    return my


def sannbunn_second(mx, MX, my, MY):
    cnt = 100
    while cnt > 0:
        x1 = (2 * mx + MX) / 3
        x2 = (mx + 2 * MX) / 3
        yy1 = sannbunn_first(x1, my, MY)
        v1 = calc_kyori(complex(x1, yy1), C)
        yy2 = sannbunn_first(x2, my, MY)
        v2 = calc_kyori(complex(x2, yy2), C)
        if v2 < v1:
            mx = x1
        else:
            MX = x2
        cnt -= 1
    return mx, yy1, v1


if n == 2:
    ans = abs(C[0] - C[1]) / 2
else:
    rx, ry, ans = sannbunn_second(0, 1000, 0, 1000)
    # ans = calc_kyori(complex(rx, ry), C)
print(ans)
