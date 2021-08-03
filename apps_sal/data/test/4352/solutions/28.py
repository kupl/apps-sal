def solve():
    A, B = map(int, input().split())
    if A == B:
        print('Draw')
    elif A == 1 or (B != 1 and B < A):
        print('Alice')
    else:
        print('Bob')


def __starting_point():
    solve()


__starting_point()
