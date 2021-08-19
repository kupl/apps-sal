def solve():
    S = input()
    a = int(input())
    hh = int(S[:2])
    mm = int(S[3:])
    mm += a
    hh += mm // 60
    mm %= 60
    hh %= 24
    print('%02d:%02d' % (hh, mm))


def __starting_point():
    solve()


__starting_point()
