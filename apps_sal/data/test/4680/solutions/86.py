(a, b, c) = list(map(int, input().split()))
if a % 5 != 0 and a % 7 != 0:
    print('NO')
elif b % 5 != 0 and b % 7 != 0:
    print('NO')
elif c % 5 != 0 and c % 7 != 0:
    print('NO')
elif a % 7 == 0:
    if b % 5 == 0 and c % 5 == 0:
        print('YES')
    else:
        print('NO')
elif b % 7 == 0:
    if a % 5 == 0 and c % 5 == 0:
        print('YES')
    else:
        print('NO')
elif a % 5 == 0 and b % 5 == 0:
    print('YES')
else:
    print('NO')
