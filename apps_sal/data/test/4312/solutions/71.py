def __starting_point():
    (a, b, c, d) = list(map(int, input().split()))
    while True:
        if c - b <= 0:
            print('Yes')
            break
        c -= b
        if a - d <= 0:
            print('No')
            break
        a -= d


__starting_point()
