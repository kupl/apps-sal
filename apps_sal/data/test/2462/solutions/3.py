for _ in range(int(input())):
    N = int(input())
    if N > 30:
        print('YES')
        if N - 30 == 6:
            print(6, 10, 15, 5)
        elif N - 30 == 10:
            print(6, 10, 15, 9)
        elif N - 30 == 14:
            print(6, 10, 15, 13)
        else:
            print(6, 10, 14, N - 30)
    else:
        print('NO')
