import sys
from functools import lru_cache
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    (N, X) = list(map(int, readline().split()))
    A = [0] * (N + 1)
    B = [0] * (N + 1)
    A[0] = B[0] = 1
    for i in range(N):
        A[i + 1] = 2 * A[i] + 3
        B[i + 1] = 2 * B[i] + 1

    def rec(i, x):
        if i == 0:
            return 1 if x > 0 else 0
        elif x <= 1 + A[i - 1]:
            return rec(i - 1, x - 1)
        else:
            return B[i - 1] + 1 + rec(i - 1, x - 2 - A[i - 1])
    print(rec(N, X))
    return


def __starting_point():
    main()


__starting_point()
