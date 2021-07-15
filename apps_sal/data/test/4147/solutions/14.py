import sys
from functools import lru_cache

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, A, B, C = list(map(int, readline().split()))
    (*L,) = list(map(int, read().split()))

    @lru_cache(maxsize=None)
    def rec(i, a, b, c):
        if i == N:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else INF

        res0 = rec(i + 1, a, b, c)
        res1 = rec(i + 1, a + L[i], b, c) + 10
        res2 = rec(i + 1, a, b + L[i], c) + 10
        res3 = rec(i + 1, a, b, c + L[i]) + 10

        return min(res0, res1, res2, res3)

    print((rec(0, 0, 0, 0)))
    return


def __starting_point():
    main()

__starting_point()
