t = int(input())
for i in range(t):
    n = int(input())
    if n <= 30:
        print('NO')
    else:
        print('YES')
        if n - 30 != 6 and n - 30 != 10 and (n - 30 != 14):
            print(str(6) + ' ' + str(10) + ' ' + str(14) + ' ' + str(n - 30))
        else:
            print(str(6) + ' ' + str(10) + ' ' + str(15) + ' ' + str(n - 31))
