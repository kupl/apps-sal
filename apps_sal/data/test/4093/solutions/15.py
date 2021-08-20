def solve():
    (n, m) = map(int, input().split(' '))
    if n == 1:
        print(0)
    elif n == 2:
        print(m)
    else:
        print(2 * m)


def __starting_point():
    t = int(input())
    for tc in range(t):
        solve()


__starting_point()
