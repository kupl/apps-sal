import math
sqa = list(map(int, input().split()))
sqb = list(map(int, input().split()))
sq1 = []
sq2 = []


def get_coords(seq, dest):
    (a, b) = (0, 1)
    for i in range(4):
        dest.append((seq[a], seq[b]))
        a += 2
        b += 2


def check_pt(p1, p2, p3):
    if p1[0] - p2[0] == 0 and p3[0] == p1[0] and (abs(p3[1]) <= abs(p1[1] - p2[1])):
        print(1)
        return 1
    elif p1[1] - p2[1] == 0 and p3[1] == p1[1] and (abs(p3[0]) <= abs(p1[0] - p2[0])):
        print(2)
        return 1
    elif p1[0] - p2[0] != 0:
        print(3)
        ab = math.sqrt(math.pow(p3[0] - p1[0], 2) + math.pow(p3[1] - p1[1], 2))
        bc = math.sqrt(math.pow(p3[0] - p2[0], 2) + math.pow(p3[1] - p2[1], 2))
        ac = math.sqrt(math.pow(p2[0] - p1[0], 2) + math.pow(p2[1] - p1[1], 2))
        return ab + bc == ac
    else:
        print(4)
        return 0


def pt_in(r, P):
    areaRectangle = 0.5 * abs((r[0][1] - r[2][1]) * (r[3][0] - r[1][0]) + (r[1][1] - r[3][1]) * (r[0][0] - r[2][0]))
    ABP = 0.5 * (r[0][0] * (P[1] - r[1][1]) + P[0] * (r[1][1] - r[0][1]) + r[1][0] * (r[0][1] - P[1]))
    BCP = 0.5 * (r[2][0] * (P[1] - r[1][1]) + P[0] * (r[1][1] - r[2][1]) + r[1][0] * (r[2][1] - P[1]))
    CDP = 0.5 * (r[2][0] * (P[1] - r[3][1]) + P[0] * (r[3][1] - r[2][1]) + r[3][0] * (r[2][1] - P[1]))
    DAP = 0.5 * (r[0][0] * (P[1] - r[3][1]) + P[0] * (r[3][1] - r[0][1]) + r[3][0] * (r[0][1] - P[1]))
    return areaRectangle == abs(ABP) + abs(BCP) + abs(CDP) + abs(DAP)


def mid_in(r, b):
    x = (b[0][0] + b[2][0]) / 2
    y = (b[1][1] + b[3][1]) / 2
    P = (x, y)
    return pt_in(r, P)


get_coords(sqa, sq1)
get_coords(sqb, sq2)


def check():
    flag = 0
    for j in range(4):
        'if check_pt(sq2[0],sq2[1],sq1[j]) or check_pt(sq2[1],sq2[2],sq1[j]) or check_pt(sq2[2],sq2[3],sq1[j]) or check_pt(sq2[0],sq2[3],sq1[j]):\n            print(5)\n            flag = 1\n            break\n        if check_pt(sq1[0],sq1[1],sq2[j]) or check_pt(sq1[1],sq1[2],sq2[j]) or check_pt(sq1[2],sq1[3],sq2[j]) or check_pt(sq1[0],sq1[3],sq2[j]):\n            print(6)\n            flag = 1\n            break'
        if pt_in(sq1, sq2[j]) or pt_in(sq2, sq1[j]):
            flag = 1
            break
    if mid_in(sq1, sq2) or mid_in(sq2, sq1):
        flag = 1
    if flag == 1:
        print('YES')
    else:
        print('NO')


check()
