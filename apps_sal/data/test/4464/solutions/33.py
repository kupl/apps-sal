def __starting_point():
    (a, b, c) = map(int, input().split())
    for i in range(1000000):
        m = a * i % b
        if m == c:
            print('YES')
            return
    print('NO')


__starting_point()
