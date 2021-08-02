def solve(a, b):
    if a * b % 2 == 0:
        print('Even')
    else:
        print('Odd')


def __starting_point():
    a, b = list(map(int, input().split()))
    solve(a, b)


__starting_point()
