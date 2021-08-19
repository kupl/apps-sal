input()
a = input()
field = [[' ' for j in range(500)] for i in range(500)]
mxb = -1
b = 0
for i in range(len(a)):
    if a[i] == '[':
        b += 1
    else:
        b -= 1
    mxb = max(mxb, b)
m = (mxb * 2 + 1) // 2


def opn(curpos, curb):
    up = mxb - curb + 1
    for i in range(up):
        field[m + i][curpos] = '|'
    for i in range(up):
        field[m - i][curpos] = '|'
    field[m + up][curpos] = '+'
    field[m - up][curpos] = '+'
    field[m + up][curpos + 1] = '-'
    field[m - up][curpos + 1] = '-'


def clos(curpos, curb):
    up = mxb - curb + 1
    for i in range(up):
        field[m + i][curpos] = '|'
    for i in range(up):
        field[m - i][curpos] = '|'
    field[m + up][curpos] = '+'
    field[m - up][curpos] = '+'
    field[m + up][curpos - 1] = '-'
    field[m - up][curpos - 1] = '-'


curb = 0
pos = 0
for i in range(len(a)):
    if a[i] == '[':
        curb += 1
        opn(pos, curb)
        pos += 1
    else:
        if a[i - 1] == '[':
            pos += 3
        clos(pos, curb)
        curb -= 1
        pos += 1
ans = []
for i in range(len(field)):
    lst = -1
    for j in range(len(field[0])):
        if field[i][j] != ' ':
            lst = j
    ans.append(lst + 1)
for i in range(len(field)):
    for j in range(ans[i]):
        print(field[i][j], end='')
    if ans[i]:
        print()
