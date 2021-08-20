def rook(r1, c1, r2, c2):
    if r1 == r2 or c1 == c2:
        return 1
    else:
        return 2


def king(r1, c1, r2, c2):
    x = abs(c1 - c2)
    y = abs(r1 - r2)
    return max(x, y)


def bishop(r1, c1, r2, c2):
    if not (r1 + c1) % 2 == (r2 + c2) % 2:
        return 0
    x = abs(r1 - r2)
    y = abs(c1 - c2)
    if x == y:
        return 1
    return 2


def __starting_point():
    (r1, c1, r2, c2) = [int(x) for x in input().split()]
    r = rook(r1, c1, r2, c2)
    b = bishop(r1, c1, r2, c2)
    k = king(r1, c1, r2, c2)
    print(str(r) + ' ' + str(b) + ' ' + str(k))


__starting_point()
