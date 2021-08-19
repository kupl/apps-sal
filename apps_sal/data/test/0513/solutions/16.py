def solve():
    S = set()
    x = [-1] * 3
    y = [-1] * 3
    xc = [0] * 3
    yc = [0] * 3
    i = 0
    for i in range(8):
        (xi, yi) = list(map(int, input().split()))
        if str([xi, yi]) in S:
            return 0
        S.add(str([xi, yi]))
        j = 0
        while j < 3:
            if x[j] == -1:
                x[j] = xi
                xc[j] += 1
                break
            elif x[j] == xi:
                xc[j] += 1
                break
            j += 1
        if j == 3:
            return 0
        j = 0
        while j < 3:
            if y[j] == -1:
                y[j] = yi
                yc[j] += 1
                break
            elif y[j] == yi:
                yc[j] += 1
                break
            j += 1
        if j == 3:
            return 0
    i = 0
    while i < 3:
        if xc[i] == 2:
            (x[i], x[1]) = (x[1], x[i])
            (xc[i], xc[1]) = (xc[1], xc[i])
            break
        i += 1
    if i == 3:
        return 0
    if xc[0] != 3 or xc[2] != 3:
        return 0
    if x[0] > x[2]:
        (x[0], x[2]) = (x[2], x[0])
    if x[0] > x[1] or x[1] > x[2]:
        return 0
    i = 0
    while i < 3:
        if yc[i] == 2:
            (y[i], y[1]) = (y[1], y[i])
            (yc[i], yc[1]) = (yc[1], yc[i])
            break
        i += 1
    if i == 3:
        return 0
    if yc[0] != 3 or yc[2] != 3:
        return 0
    if y[0] > y[2]:
        (y[0], y[2]) = (y[2], y[0])
    if y[0] > y[1] or y[1] > y[2]:
        return 0
    return 1


if solve() == 1:
    print('respectable')
else:
    print('ugly')
