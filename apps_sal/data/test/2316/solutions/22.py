for _ in range(int(input())):
    x, n, m = tuple(map(int, input().split()))

    while x > 20 and n > 0:
        x = x // 2 + 10
        n -= 1

    while x > 0 and m > 0:
        x -= 10
        m -= 1

    if x <= 0:
        print('YES')
    else:
        print('NO')

