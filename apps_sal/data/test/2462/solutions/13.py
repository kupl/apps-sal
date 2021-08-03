for _ in range(int(input())):
    n = int(input())
    if n <= 30:
        print('NO')
    else:
        print('YES')
        if n - 30 == 6:
            print(6, 10, 15, 5)
        elif n - 30 == 10:
            print(6, 10, 15, 9)
        elif n - 30 == 14:
            print(6, 10, 13, 15)
        else:
            print(6, 10, 14, n - 30)
