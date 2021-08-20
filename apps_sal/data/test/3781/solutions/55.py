import sys
from collections import Counter


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
    for _ in range(read_int()):
        N = read_int()
        a = read_int_list()
        if N % 2:
            print('Second')
            continue
        cnt = Counter(a)
        for val in list(cnt.values()):
            if val % 2:
                print('First')
                break
        else:
            print('Second')


def __starting_point():
    Main()


__starting_point()
