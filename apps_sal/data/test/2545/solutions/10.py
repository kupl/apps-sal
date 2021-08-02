for i in ' ' * int(input()):
    a, b = map(int, input().split())
    if (a + b) % 3 == 0:
        if 2 * a >= b and 2 * b >= a:
            print('YES')
            continue
    print('NO')
