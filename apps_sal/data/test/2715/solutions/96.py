import sys
import bisect

input = sys.stdin.readline
sys.setrecursionlimit(100000)
mod = 10 ** 9 + 7
# mod = 998244353


def read_values():
    return list(map(int, input().split()))


def read_index():
    return [int(x) - 1 for x in input().split()]


def read_list():
    return list(read_values())


def read_lists(N):
    return [read_list() for n in range(N)]


class V:
    def __init__(self, f, v=None):
        self.f = f
        self.v = v

    def __str__(self):
        return str(self.v)

    def ud(self, n):
        if n is None:
            return

        if self.v is None:
            self.v = n
            return
        self.v = self.f(self.v, n)


def main():
    K = int(input())
    N = 50
    M = K // N
    m = K % N
    k = N - m
    A = [N + M - (N - k + 1)] * k + [N + M + k] * (N - k)
    print(N)
    print((" ".join(map(str, A))))


def __starting_point():
    main()


__starting_point()
