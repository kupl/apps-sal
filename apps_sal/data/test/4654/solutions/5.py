for i in range(int(input())):
    n, k = [int(i) for i in input().split()]
    if k > n:
        print('NO')
    elif (n - k + 1) % 2 == 1 and n - k + 1 > 0:
        print('YES')
        for i in range(k - 1):
            print(1, end=' ')
        print(n - k + 1)
    elif (n - 2 * (k - 1)) % 2 == 0 and n - 2 * (k - 1) > 0:
        print('YES')
        for i in range(k - 1):
            print(2, end=' ')
        print(n - 2 * (k - 1))
    else:
        print('NO')
