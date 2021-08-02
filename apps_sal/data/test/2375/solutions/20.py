def solve():
    x, y = list(map(int, input().split()))
    if abs(x - y) <= 1:
        print('Brown')
    else:
        print('Alice')


def __starting_point():
    solve()


__starting_point()
