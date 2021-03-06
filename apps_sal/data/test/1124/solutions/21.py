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


def GCD(a: int, b: int) -> int:
    """
    ユークリッドの互除法による最大公約数/O(log min(a,b))
    """
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


def GCD_multi(vec: list) -> int:
    """
    数列の要素の最大公約数を求める/O(N log(a'))
    """
    l = vec[0]
    for i in range(len(vec) - 1):
        l = GCD(l, vec[i + 1])
    return l


def main():
    n = read_int()
    A = read_ints_list()
    print(GCD_multi(A))


def __starting_point():
    main()


__starting_point()
