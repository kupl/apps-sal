for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    if k % 2 == 1:
        if n % 2 == 0:
            if 2 * k <= n:
                print('YES')
                print(*[2] * (k - 1), n - 2 * (k - 1))
            else:
                print('NO')
        else:
            if k <= n:
                print('YES')
                print(*[1] * (k - 1), n - k + 1)
            else:
                print('NO')
    else:
        if k <= n and n % 2 == 0:
            print('YES')
            print(*[1] * (k - 1), n - k + 1)
        else:
            print('NO')
