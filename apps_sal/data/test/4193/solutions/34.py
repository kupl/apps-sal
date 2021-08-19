import math


def i_input():
    return int(input())


def i_map():
    return map(int, input().split())


def i_list():
    return list(map(int, input().split()))


def i_row(N):
    return [int(input()) for _ in range(N)]


def i_row_list(N):
    return [list(map(int, input().split())) for _ in range(N)]


aaa = i_row_list(3)
n = i_input()
b = i_row(n)
ans = 'No'
for i in range(3):
    for j in range(3):
        if aaa[i][j] in b:
            aaa[i][j] = 0
xlos1 = 0
xlos2 = 0
for i in range(3):
    colm = 0
    rows = 0
    for j in range(3):
        colm += aaa[i][j]
        rows += aaa[j][i]
    xlos1 += aaa[i][i]
    xlos2 += aaa[2 - i][i]
    if colm == 0 or rows == 0:
        ans = 'Yes'
        break
if ans != 'Yes':
    if xlos1 == 0 or xlos2 == 0:
        ans = 'Yes'
print(ans)
