import sys


def solve():
    input = sys.stdin.readline
    N, Z, W = map(int, input().split())
    A = [int(a) for a in input().split()]
    if N == 1:
        print(abs(W - A[0]))
    else:
        print(max(abs(W - A[N - 1]), abs(A[N - 2] - A[N - 1])))

    return 0


def __starting_point():
    solve()


__starting_point()
