def get_place(rows, dpr, k):
    k -= 1
    dn = k // 2
    return (dn // dpr + 1, dn % dpr + 1, 'LR'[k % 2])


def m():
    print(*get_place(*list(map(int, input().split(' ')))))


def __starting_point():
    m()


__starting_point()
