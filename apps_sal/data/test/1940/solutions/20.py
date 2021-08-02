def R():
    return [int(x) for x in input().split()]


def __starting_point():
    n, k = R()
    w = R()
    result = 0
    for _w in w:
        if _w < k:
            result += 1
        elif _w % k == 0:
            result += _w // k
        else:
            result += _w // k + 1

    if result % 2 == 0:
        print(result // 2)
    else:
        print(result // 2 + 1)


__starting_point()
