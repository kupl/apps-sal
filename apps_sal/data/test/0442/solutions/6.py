r = int(input())

if r%2 == 0:
    print('NO')

elif r == 1:
    print('NO')

elif r == 3:
    print('NO')
else:
    print(1, end=' ')
    print((r-3)//2)
