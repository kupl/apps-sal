import sys


def read_str(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline().strip())
def read_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def read_str_split(): return list(sys.stdin.readline().strip())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))


def Main():
    n = read_int()
    a = read_int_list()
    ans = [0] * n
    ans[0] = sum(a) - 2 * sum(a[1::2])
    for i in range(1, n):
        ans[i] = 2 * a[i - 1] - ans[i - 1]
    print((*ans))


def __starting_point():
    Main()


__starting_point()
