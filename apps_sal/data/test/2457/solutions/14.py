import sys


def noop(*object):
    return


def main():
    T = read_int()
    for case_idx in range(T):
        ans = solve_case()
        sys.stdout.write('{}\n'.format(ans))


def solve_case():
    (n, a, b, c, d) = read_int_list()
    if (a - b) * n > c + d or (a + b) * n < c - d:
        return 'No'
    return 'Yes'


def read_str():
    return input()


def read_int():
    return int(input())


def read_str_list():
    return input().split(' ')


def read_int_list():
    return list(map(int, input().split(' ')))


def read_lines(n, read_func):
    return [read_func() for _ in range(n)]


def list_to_str(l, sep=' '):
    return sep.join(map(str, l))


l2s = list_to_str


def make_list(shape, value=None):
    if len(shape) == 1:
        return [value] * shape[0]
    return [make_list(shape[1:], value) for _ in range(shape[0])]


def __starting_point():
    sys.setrecursionlimit(1000000)
    main()


__starting_point()
