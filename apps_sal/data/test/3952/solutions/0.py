import sys
import copy
input = sys.stdin.readline
n = int(input())
P = [list(map(int, input().split())) for i in range(n)]
SET_X = set()
SET_Y = set()
for (x, y) in P:
    SET_X.add(x)
    SET_Y.add(y)
CX = sorted(SET_X)
CY = sorted(SET_Y)
LEN = len(CX)
MAX = len(CX) - 1
DICT_X = {x: i for (i, x) in enumerate(CX)}
DICT_Y = {x: i for (i, x) in enumerate(CY)}
for i in range(n):
    P[i] = [DICT_X[P[i][0]], DICT_Y[P[i][1]]]
check = [0] * len(CX)
BIT = [0] * (LEN + 1)


def update(v, w):
    while v <= LEN:
        BIT[v] += w
        v += v & -v


def getvalue(v):
    ANS = 0
    while v != 0:
        ANS += BIT[v]
        v -= v & -v
    return ANS


LIST_Y = [[] for i in range(len(CY))]
for (x, y) in P:
    LIST_Y[y].append(x)
for i in range(len(CY)):
    LIST_Y[i].sort()
ANS = 0
for y in range(len(CY) - 1, -1, -1):
    for x in LIST_Y[y]:
        if check[x] == 0:
            check[x] = 1
            update(x + 1, 1)
    ANS += getvalue(LIST_Y[y][0] + 1) * (getvalue(MAX + 1) - getvalue(LIST_Y[y][0] + 1) + 1)
    for i in range(1, len(LIST_Y[y])):
        ANS += (getvalue(LIST_Y[y][i] + 1) - getvalue(LIST_Y[y][i - 1] + 1)) * (getvalue(MAX + 1) - getvalue(LIST_Y[y][i] + 1) + 1)
print(ANS)
