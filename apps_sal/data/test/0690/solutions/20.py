__author__ = 'Lipen'


def actions(n):
    s = ''
    for x in reversed(n):
        if x >= 5:
            q = '-O'
            w = 'O' * (x - 5) + '-' + 'O' * (9 - x)
        else:
            q = 'O-'
            w = 'O' * x + '-' + 'O' * (4 - x)
        s += q + '|' + w + '\n'
    return s[:-1]


def main():
    n = list(map(int, input()))
    print(actions(n))


def __starting_point():
    main()


__starting_point()
