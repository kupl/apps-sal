import sys
sys.setrecursionlimit(10 ** 9)
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines


def read_int():
    return int(readline())


def read_ints():
    return map(int, readline().split())


def read_ints_list():
    return list(map(int, readline().split()))


def read_ints_grid(h):
    return list((list(map(int, readline().split())) for _ in range(h)))


def read_strs_list():
    return list(map(str, readline().rstrip().split()))


def read_strs_grid(h):
    return list((list(map(str, readline().rstrip().split())) for _ in range(h)))


def read_allints_grid(w):
    grid = map(int, read().split())
    grid = list(map(list, zip(*(grid for _ in range(w)))))
    return grid


def read_allstrs_grid(w):
    grid = map(str, read().split())
    grid = list(map(list, zip(*(grid for _ in range(w)))))
    return grid


def sol():
    return None


def main():
    (n, m) = read_ints()
    if n == m == 1:
        print(1)
    elif n == 1 or m == 1:
        print(max(n, m) - 2)
    else:
        print((n - 2) * (m - 2))
    return None


def __starting_point():
    main()


__starting_point()
