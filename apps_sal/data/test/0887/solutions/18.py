n, a = int(input()), input().split()

if n == 1:
    if a[0] == '1':
        print('YES')
    else:
        print('NO')
else:
    unfst = len([x for x in a if x == '0'])
    if unfst == 1:
        print('YES')
    else:
        print('NO')

