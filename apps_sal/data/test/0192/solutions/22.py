def get_next(T):
    [a, b, c] = sorted(T)
    return [b, c, b + c - 1]


def __starting_point():
    y, x = [int(a) for a in input().split()]
    T = [x, x, x]
    # print(T)
    i = 0
    while max(T) < y:
        T = get_next(T)
        # print(T)
        i += 1

    print(2 + i)


__starting_point()
