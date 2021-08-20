def solve():
    (x, a, b) = map(int, input().split())
    if b <= a:
        print('delicious')
    elif a < b <= a + x:
        print('safe')
    else:
        print('dangerous')


def __starting_point():
    solve()


__starting_point()
