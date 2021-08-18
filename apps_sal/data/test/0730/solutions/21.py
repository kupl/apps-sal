k = int(input())
print('+------------------------+')
a = (k - 4) // 3
b = (k - 4) % 3
if k == 0:
    print('|
    print('|
    print('|
    print('|
elif k == 1:
    print('| O.
    print('|
    print('|
    print('|
elif k == 2:
    print('| O.
    print('| O.
    print('|
    print('|
elif k == 3:
    print('| O.
    print('| O.
    print('|O.......................|')
    print('|
elif k == 4:
    print('| O.
    print('| O.
    print('|O.......................|')
    print('| O.
elif b == 0:
    print('|O' + '.O' * a + '.
    print('|O' + '.O' * a + '.
    print('|O.......................|')
    print('|O' + '.O' * a + '.
elif b == 1:
    print('|O' + '.O' * (a + 1) + '.
    print('|O' + '.O' * a + '.
    print('|O.......................|')
    print('|O' + '.O' * a + '.
elif b == 2:
    print('|O' + '.O' * (a + 1) + '.
    print('|O' + '.O' * (a + 1) + '.
    print('|O.......................|')
    print('|O' + '.O' * a + '.
print('+------------------------+')
