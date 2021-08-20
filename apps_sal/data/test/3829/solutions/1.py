__author__ = 'Jacob Dlougach'


def __starting_point():
    (m, n) = map(int, input().split())
    result = 0
    for i in range(m):
        result += ((i + 1) / m) ** n
    print('{:.9}'.format(m + 1 - result))


__starting_point()
