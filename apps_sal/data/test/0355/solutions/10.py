def checkA(i, j):
    for k in range(i):
        if arr[k][j] != '.':
            return 1000
    return i


def checkB(i, j):
    for k in range(i + 1, 8):
        if arr[k][j] != '.':
            return 1000
    return 7 - i


arr = []
for i in range(8):
    a = input()
    arr.append(a)
minA = 1000
minB = 1000
for i in range(8):
    for j in range(8):
        if arr[i][j] == 'W':
            minA = min(minA, checkA(i, j))
        if arr[i][j] == 'B':
            minB = min(minB, checkB(i, j))
if minA <= minB:
    print('A')
else:
    print('B')
