import sys
from functools import lru_cache
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    (N, K, *A) = list(map(int, read().split()))
    K = list(map(int, f'{K:>040b}'))
    A2 = [list(map(int, f'{a:>040b}')) for a in A]
    B = [0] * 40
    for a in A2:
        for (i, bit) in enumerate(a):
            B[i] += bit
    for i in range(40):
        if B[i] == N - B[i]:
            B[i] = 2
        elif B[i] < N - B[i]:
            B[i] = 1
        else:
            B[i] = 0

    @lru_cache(maxsize=None)
    def rec(i, x, smaller):
        if i == 40:
            ans = 0
            for a in A:
                ans += x ^ a
            return ans
        elif smaller:
            if B[i] == 2:
                return rec(i + 1, x << 1, True)
            else:
                return rec(i + 1, (x << 1) + B[i], True)
        elif B[i] == 2:
            if K[i] == 0:
                return rec(i + 1, x << 1, False)
            else:
                return rec(i + 1, x << 1, True)
        elif K[i] == B[i]:
            return rec(i + 1, (x << 1) + K[i], False)
        elif K[i] < B[i]:
            return rec(i + 1, (x << 1) + K[i], False)
        else:
            return rec(i + 1, (x << 1) + B[i], True)
    print(rec(0, 0, False))
    return


def __starting_point():
    main()


__starting_point()
