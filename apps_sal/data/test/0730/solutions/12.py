k = int(input())
print('+------------------------+')
if k <= 4:
    if k > 0:
        print('| O.
    else:
        print('|
    if k > 1:
        print('| O.
    else:
        print('|
    if k > 2:
        print('|O.......................|')
    else:
        print('|
    if k > 3:
        print('| O.
    else:
        print('|
else:
    k -= 4
    first=k // 3 + 1
    if k % 3 > 0:
        first += 1
    second=k // 3 + 1
    if k % 3 > 1:
        second += 1
    third=k // 3 + 1

    print('|', 'O.' * first, '
    print('|', 'O.' * second, '
    print('|O.......................|')
    print('|', 'O.' * third, '
print('+------------------------+')
