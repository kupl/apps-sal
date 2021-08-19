import bisect
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


class v:

    def __init__(self, f):
        self.f = f
        self.v = None

    def __str__(self):
        return str(self.v)

    def ud(self, n):
        if self.v is None:
            self.v = n
        else:
            self.v = self.f(self.v, n)


def read_values():
    return list(map(int, input().split()))


def read_list():
    return list(read_values())


def main():
    (M, K) = read_values()
    if K >= 2 ** M:
        print(-1)
        return
    if M == 1:
        print('0 0 1 1' if K == 0 else -1)
        return
    X = [str(i) for i in range(2 ** M) if i != K]
    res = X + [str(K)] + X[::-1] + [str(K)]
    print(' '.join(res))


def __starting_point():
    main()


__starting_point()
