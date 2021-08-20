def __starting_point():
    (x, y, z) = (int(x) for x in input().split())
    (a, b, c) = (int(x) for x in input().split())
    if a < x:
        print('NO')
        quit()
    if a + b - x < y:
        print('NO')
        quit()
    if a + b + c - x - y < z:
        print('NO')
        quit()
    print('YES')


__starting_point()
