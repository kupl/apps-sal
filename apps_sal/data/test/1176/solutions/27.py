import sys


def read_str():
    return sys.stdin.readline().strip()


def read_int():
    return int(sys.stdin.readline().strip())


def read_ints():
    return list(map(int, sys.stdin.readline().strip().split()))


def read_str_split():
    return list(sys.stdin.readline().strip())


def read_int_list():
    return list(map(int, sys.stdin.readline().strip().split()))


def Main():
    N = read_int()
    A = read_int_list()
    abs_a = list(map(abs, A))
    minus_a = [v for v in A if v < 0]
    min_abs = min(abs_a)
    len_minus = len(minus_a)
    sum_abs = sum(abs_a)
    if len_minus % 2 == 0:
        print(sum_abs)
    else:
        print(sum_abs - min_abs * 2)


def __starting_point():
    Main()


__starting_point()
