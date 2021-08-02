i1 = input('').split(' ')
x1 = int(i1[0])
y1 = int(i1[1])
x2 = int(i1[2])
y2 = int(i1[3])
i1 = input('').split(' ')
x3 = int(i1[0])
y3 = int(i1[1])
x4 = int(i1[2])
y4 = int(i1[3])
i1 = input('').split(' ')
x5 = int(i1[0])
y5 = int(i1[1])
x6 = int(i1[2])
y6 = int(i1[3])


def chk(x1, y1, x2, y2, x3, y3):
    if(x3 <= x2 and x3 >= x1 and y3 >= y1 and y3 <= y2):
        return True
    else:
        return False


r11 = chk(x3, y3, x4, y4, x1, y1)
r12 = chk(x5, y5, x6, y6, x1, y1)
r21 = chk(x3, y3, x4, y4, x2, y1)
r22 = chk(x5, y5, x6, y6, x2, y1)
r31 = chk(x3, y3, x4, y4, x1, y2)
r32 = chk(x5, y5, x6, y6, x1, y2)
r41 = chk(x3, y3, x4, y4, x2, y2)
r42 = chk(x5, y5, x6, y6, x2, y2)


def car(x1, y1, x2, y2, x3, y3, x4, y4):
    yy1 = max(y1, y3)
    yy2 = min(y2, y4)
    xx1 = max(x1, x3)
    xx2 = min(x2, x4)
    area = (abs(yy1 - yy2)) * (abs(xx1 - xx2))
    return area


if((r11 or r12) and (r21 or r22) and (r31 or r32) and (r41 or r42)):
    a1 = car(x1, y1, x2, y2, x3, y3, x4, y4)
    a2 = car(x1, y1, x2, y2, x5, y5, x6, y6)
    ta = a1 + a2
    if(ta >= (x2 - x1) * (y2 - y1)):
        print('NO')
    else:
        print('YES')
else:
    print('YES')
