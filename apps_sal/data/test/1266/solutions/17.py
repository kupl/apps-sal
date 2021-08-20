def in_ls(name_type, string):
    string = string.split()
    string = map(name_type, string)
    string = list(string)
    return string


n = int(input())
king = in_ls(int, input())
cord = {}
for i in range(0, n):
    in_str = input().split()
    x = int(in_str[1])
    y = int(in_str[2])
    cord[x, y] = in_str[0]
nearest = []
for i in range(0, 8):
    nearest.append((1000000000000000000, 0))
for el in cord.keys():
    res = (el[0] - king[0], el[1] - king[1])
    if res[0] == 0:
        if res[1] > 0:
            if abs(res[1]) < nearest[0][0]:
                nearest[0] = (abs(res[1]), el)
        elif abs(res[1]) < nearest[4][0]:
            nearest[4] = (abs(res[1]), el)
    if res[1] == 0:
        if res[0] > 0:
            if abs(res[0]) < nearest[6][0]:
                nearest[6] = (abs(res[0]), el)
        elif abs(res[0]) < nearest[2][0]:
            nearest[2] = (abs(res[0]), el)
    if abs(res[0]) == abs(res[1]):
        if res[0] > 0 and res[1] > 0:
            if abs(res[0]) < nearest[7][0]:
                nearest[7] = (abs(res[0]), el)
        if res[0] < 0 and res[1] > 0:
            if abs(res[0]) < nearest[1][0]:
                nearest[1] = (abs(res[0]), el)
        if res[0] < 0 and res[1] < 0:
            if abs(res[0]) < nearest[3][0]:
                nearest[3] = (abs(res[0]), el)
        if res[0] > 0 and res[1] < 0:
            if abs(res[0]) < nearest[5][0]:
                nearest[5] = (abs(res[0]), el)
check = False
for i in range(8):
    if nearest[i][1] != 0:
        if i in [1, 3, 5, 7]:
            if cord[nearest[i][1]] == 'Q' or cord[nearest[i][1]] == 'B':
                check = True
        elif cord[nearest[i][1]] == 'R' or cord[nearest[i][1]] == 'Q':
            check = True
if check:
    print('YES')
else:
    print('NO')
