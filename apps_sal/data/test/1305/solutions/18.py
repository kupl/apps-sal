n = input()
b = True
Meta = {'25': 0, '50': 0, '100': 0}
i25 = 0
i50 = 0
Data = input().split(' ')
for item in Data:
    if item == '25':
        i25 += 1
    elif item == '50':
        i50 += 1
        if i25 == 0:
            b = False
            break
        else:
            i25 -= 1
    elif item == '100':
        if i25 == 0 and i50 == 0:
            b = False
            break
        elif i50 >= 1 and i25 >= 1:
            i50 -= 1
            i25 -= 1
        elif i25 >= 3:
            i25 -= 3
        else:
            b = False
            break
if b:
    print('YES')
else:
    print('NO')
