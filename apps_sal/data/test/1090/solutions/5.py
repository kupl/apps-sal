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
    (n, k) = read_ints()
    s = read_str()
    cnt = s.count('RL') + s.count('LR') + 1
    cnt = min(n - 1, n - cnt + 2 * k)
    print(cnt)


def __starting_point():
    Main()


__starting_point()
