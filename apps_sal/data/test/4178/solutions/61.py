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
    n = INT()
    h = LIST()
    for i in range(n - 1):
        if h[i] < h[i + 1]:
            h[i + 1] -= 1
    flg = True
    for i in range(n - 1):
        if h[i] > h[i + 1]:
            flg = False
    if flg:
        print('Yes')
    else:
        print('No')


def __starting_point():
    do()


__starting_point()
