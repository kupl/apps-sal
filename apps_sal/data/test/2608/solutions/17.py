import sys
input = sys.stdin.readline

testcase = int(input())
T = [list(map(int, input().split())) for i in range(testcase * 3)]
# n,m=map(int,input().split())
# WHITE=list(map(int,input().split()))
# BLACK=list(map(int,input().split()))


def COMMON(WHITE, BLACK):
    x1, y1, x2, y2 = WHITE
    x3, y3, x4, y4 = BLACK
    return (max(x1, x3), max(y1, y3), min(x2, x4), min(y2, y4))


def BtoW(WHITE):
    x1, y1, x2, y2 = WHITE
    if (x1 + y1) % 2 == 0:
        return (x2 - x1 + 1) * (y2 - y1 + 1) // 2
    else:
        return (x2 - x1 + 1) * (y2 - y1 + 1) - (x2 - x1 + 1) * (y2 - y1 + 1) // 2


def WtoB(BLACK):
    x1, y1, x2, y2 = BLACK
    if (x1 + y1) % 2 == 1:
        return (x2 - x1 + 1) * (y2 - y1 + 1) // 2
    else:
        return (x2 - x1 + 1) * (y2 - y1 + 1) - (x2 - x1 + 1) * (y2 - y1 + 1) // 2


for test in range(testcase):
    n, m = T[test * 3]
    WHITE = T[test * 3 + 1]
    BLACK = T[test * 3 + 2]

    ANSB = n * m // 2
    ANSW = n * m - ANSB

    # print(ANSB,ANSW,end="!")

    WHITE2 = COMMON(WHITE, BLACK)

    k = BtoW(WHITE)
    ANSB -= k
    ANSW += k

    # print(ANSB,ANSW,end="!")

    # print(x5,y5,x6,y6)
    if WHITE2[0] > WHITE2[2] or WHITE2[1] > WHITE2[3]:  # 共通部なし
        True
    else:
        l = BtoW(WHITE2)
        ANSB += l
        ANSW -= l

    # print(ANSB,ANSW,end="!")

    m = WtoB(BLACK)

    ANSB += m
    ANSW -= m

    print(ANSW, ANSB)
