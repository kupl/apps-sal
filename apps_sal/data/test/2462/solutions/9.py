for _ in range(int(input())):
    n = int(input())
    if n < 31:
        print('NO')
    else:
        print('YES')
        if n != 36 and n != 40 and (n != 44):
            print(6, 10, 14, n - 30)
        else:
            print(6, 10, 15, n - 31)
