a, b, c = list(map(int, input().split()))


def __starting_point():
    if (b - a) == (c - b):
        print('YES')
    else:
        print('NO')


__starting_point()
