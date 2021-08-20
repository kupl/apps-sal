def INT():
    return int(input())


def INTM():
    return map(int, input().split())


def STRM():
    return map(str, input().split())


def STR():
    return str(input())


def LIST():
    return list(map(int, input().split()))


def LISTS():
    return list(map(str, input().split()))


def do():
    (w, h, x, y) = INTM()
    cx = w / 2
    cy = h / 2
    flg = 0
    if cx == x and cy == y:
        flg = 1
    print(w * h / 2, flg)


def __starting_point():
    do()


__starting_point()
