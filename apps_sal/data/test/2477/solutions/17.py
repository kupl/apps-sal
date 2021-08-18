
def solve(*args: str) -> str:
    n, k = list(map(int, args[0].split()))
    A = tuple(map(int, args[1].split()))

    l, r = 1, max(A)
    while 0.1 < r - l:
        m = (l + r) / 2
        cnt = 0
        for a in A:
            cnt += -int(-a // m) - 1

        if k < cnt:
            l = m
        else:
            r = m

    return str(-int(-l // 1))


def __starting_point():
    print((solve(*(open(0).read().splitlines()))))


__starting_point()
