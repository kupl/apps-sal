for f in range(int(input())):
    (n, k) = map(int, input().split())
    if k % 2 == 0:
        if n % 2 == 0:
            if n < k:
                print('NO')
            else:
                print('YES')
                sol = [1] * k
                sol[0] = n - k + 1
                print(*sol)
        else:
            print('NO')
    elif n % 2 == 0:
        if 2 * k > n:
            print('NO')
        else:
            print('YES')
            sol = [2] * k
            sol[0] = n - 2 * k + 2
            print(*sol)
    elif k > n:
        print('NO')
    else:
        print('YES')
        sol = [1] * k
        sol[0] = n - k + 1
        print(*sol)
