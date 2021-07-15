n = int(input())
a = [int(s) for s in input().split(' ')]
col = 0
b = [0, 0, 0, 0, 0, 0]
for el in a:
    if el == 4:
        b[0] += 1
    elif el == 8:
        if b[0] > 0:
            b[0] -= 1
            b[1] += 1
        else:
            col += 1
    elif el == 15:
        if b[1] > 0:
            b[1] -= 1
            b[2] += 1
        else:
            col += 1
    elif el == 16:
        if b[2] > 0:
            b[2] -= 1
            b[3] += 1
        else:
            col += 1
    elif el == 23:
        if b[3] > 0:
            b[3] -= 1
            b[4] += 1
        else:
            col += 1
    elif el == 42:
        if b[4] > 0:
            b[4] -= 1
            b[5] += 1
        else:
            col += 1
    else:
        col += 1
col += b[0] + 2*b[1] + 3*b[2] + 4*b[3] + 5*b[4]
print(col)
