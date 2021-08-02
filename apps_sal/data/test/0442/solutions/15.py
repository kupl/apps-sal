r = int(input())

if r >= 5:
    if r % 2 == 0:
        print('NO')
    else:
        y = int((r - 3) / 2)
        print(1, '', y)
else:
    print('NO')
