n = int(input())
if n % 10 == 1:
    print('NO')
elif n % 10 == 7:
    print('NO')
elif n % 10 == 9:
    print('NO')
elif 13 <= n <= 29 or n == 10:
    print('NO')
elif 70 <= n <= 79:
    print('NO')
elif 90 <= n <= 99:
    print('NO')
else:
    print('YES')
