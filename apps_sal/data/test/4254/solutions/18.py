def __starting_point():
    (s, w) = list(map(int, input().split()))
    if s > w:
        print('safe')
    else:
        print('unsafe')


__starting_point()
