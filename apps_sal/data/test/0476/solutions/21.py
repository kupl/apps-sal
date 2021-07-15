number = input()
l = len(number)

if number[0] != '1':
    print('NO')
elif number.count('1')+number.count('4') != l:
    print('NO')
elif number.count('444') != 0:
    print('NO')
else:
    print('YES')
