for test in range(int(input())):
    n = int(input())
    c = 6 + 10 + 14
    if n - c >= 1:
        print('YES')
        if n - c == 6 or n - c == 10 or n - c == 14:
            print(6, 10, 15, n - c - 1)
        else:
            print(6, 10, 14, n - c)
    else:
        print('NO')
