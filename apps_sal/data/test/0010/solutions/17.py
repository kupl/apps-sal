def solve():
    N = int(input())

    n7 = N // 7
    m7 = N % 7
    ma = n7 * 2 + min(m7, 2)
    mi = n7 * 2
    if m7 == 6:
        mi += 1

    print(mi, ma)


def __starting_point():
    solve()

__starting_point()
