def vaild(i, j):
    per = 1
    per1 = 1
    per2 = 1
    per3 = 1
    for t in range(i - 1, -1, -1):
        if A[t][j] == 'x':
            per += 1
        else:
            break
    for t in range(i + 1, 4):
        if A[t][j] == 'x':
            per += 1
        else:
            break
    if per >= 3:
        return True
    for t in range(j - 1, -1, -1):
        if A[i][t] == 'x':
            per1 += 1
        else:
            break
    for t in range(j + 1, 4):
        if A[i][t] == 'x':
            per1 += 1
        else:
            break
    if per1 >= 3:
        return True
    i1 = i - 1
    j1 = j - 1
    i2 = i + 1
    j2 = j + 1
    while (i1 >= 0 and j1 >= 0):
        if A[i1][j1] == 'x':
            i1 -= 1
            j1 -= 1
            per2 += 1
        else:
            break
    while (i2 <= 3 and j2 <= 3):
        if A[i2][j2] == 'x':
            per2 += 1
            i2 += 1
            j2 += 1
        else:
            break
    if per2 >= 3:
        return True
    i3 = i - 1
    j3 = j + 1
    while (i3 >= 0 and j3 <= 3):
        if A[i3][j3] == 'x':
            i3 -= 1
            j3 += 1
            per3 += 1
        else:
            break
    i4 = i + 1
    j4 = j - 1
    while (i4 <= 3 and j4 >= 0):
        if A[i4][j4] == 'x':
            i4 += 1
            j4 -= 1
            per3 += 1
        else:
            break
    if per3 >= 3:
        return True
    return False


A = [0] * 4
for j in range(4):
    A[j] = input()
s = 0
for i in range(4):
    for j in range(4):
        if A[i][j] == '.':

            if vaild(i, j):
                s = 1
                break
if s == 1:
    print('YES')
else:
    print('NO')
