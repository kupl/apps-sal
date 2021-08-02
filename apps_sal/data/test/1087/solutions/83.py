import sys
from functools import lru_cache

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K, *A = list(map(int, read().split()))

    K = list(map(int, f'{K:>040b}'))
    A_bin = [list(map(int, f'{a:>040b}')) for a in A]

    B = [0] * 40
    for a in A_bin:
        for i, bit in enumerate(a):
            B[i] += bit

    B = [1 if b < N - b else 0 for b in B]

    @lru_cache(maxsize=None)
    def rec(i, x, smaller):
        if i == 40:
            ans = 0
            for a in A:
                ans += x ^ a
            return ans
        elif smaller:
            return rec(i + 1, (x << 1) + B[i], True)
        elif K[i] <= B[i]:
            return rec(i + 1, (x << 1) + K[i], False)
        else:
            return rec(i + 1, (x << 1) + B[i], True)

    print((rec(0, 0, False)))
    return


def __starting_point():
    main()


__starting_point()
