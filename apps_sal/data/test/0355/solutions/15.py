
import time


a = [[0 for j in range(8)] for i in range(8)]

for i in range(8):
    b = input()
    for j in range(8):
        a[j][i] = b[j]

start = time.time()

mW = 10
mB = 10

for i in range(8):
    flag = True
    for j in range(8):
        if a[i][j] == 'B':
            flag = False
            break
        if a[i][j] == 'W':
            break
    if flag == False:
        continue
    if mW > j:
        mW = j

for i in range(8):
    flag = True
    for j in range(8):
        if a[i][7 - j] == 'W':
            flag = False
            break
        if a[i][7 - j] == 'B':
            break
    if flag == False:
        continue
    if mB > j:
        mB = j


if mW <= mB:
    print('A')
else:
    print('B')
finish = time.time()
