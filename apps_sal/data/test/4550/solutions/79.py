def solve():
    a, b, c = map(int, input().split())
    if a == b + c or b == a + c or c == a + b:
        print('Yes')
    else:
        print('No')


def __starting_point():
    solve()


__starting_point()
