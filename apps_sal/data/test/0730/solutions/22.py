import math


k = int(input())


def row(x, y):
    print('|O.' + 'O.' * x + '



print('+------------------------+')
if k == 0:
    print('|
    print('|
    print('|
    print('|
    print('+------------------------+')
    quit()
if k == 1:
    print('| O.
    print('|
    print('|
    print('|
    print('+------------------------+')
    quit()
if k == 2:
    print('| O.
    print('| O.
    print('|
    print('|
    print('+------------------------+')
    quit()
if k == 3:
    print('| O.
    print('| O.
    print('|O.......................|')
    print('|
    print('+------------------------+')
    quit()
if k == 4:
    print('| O.
    print('| O.
    print('|O.......................|')
    print('| O.
    print('+------------------------+')
    quit()

if ((k - 4) % 3) == 1:
    row(math.ceil((k - 4) / 3), 'D|)')
    row(math.ceil((k - 4) / 3) - 1, '.|')
    print('|O.......................|')
    row(math.ceil((k - 4) / 3) - 1, '.|)')
if ((k - 4) % 3) == 2:
    row(math.ceil((k - 4) / 3), 'D|)')
    row(math.ceil((k - 4) / 3), '.|')
    print('|O.......................|')
    row(math.ceil((k - 4) / 3) - 1, '.|)')
if ((k - 4) % 3) == 0:
    row(math.ceil((k - 4) / 3), 'D|)')
    row(math.ceil((k - 4) / 3), '.|')
    print('|O.......................|')
    row(math.ceil((k - 4) / 3), '.|)')
print('+------------------------+')
