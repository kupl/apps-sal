import sys

inf = 1 << 60


def solve():
    p, x, y = map(int, input().split())

    for s in range(x, y - 1, -50):
        if p in list_tshirt(s):
            print(0)
            return

    for i in range(1, 476):
        s = x + i * 50

        if p in list_tshirt(s):
            print((i + 1) // 2)
            return


def list_tshirt(s):
    res = [0] * 25
    i = (s // 50) % 475

    for k in range(25):
        i = (i * 96 + 42) % 475
        res[k] = i + 26

    return res


def __starting_point():
    solve()


__starting_point()
