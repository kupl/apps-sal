import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, q = list(map(int, input().split()))
    S = [-f_inf] + list(int(input()) for _ in range(a)) + [f_inf]
    T = [-f_inf] + list(int(input()) for _ in range(b)) + [f_inf]

    for _ in range(q):
        res = f_inf
        x = int(input())

        idx_s = bisect_left(S, x)
        idx_t = bisect_left(T, x)
        for s in [S[idx_s - 1], S[idx_s]]:
            for t in [T[idx_t - 1], T[idx_t]]:
                d1 = abs(s - x) + abs(s - t)
                d2 = abs(t - x) + abs(t - s)
                res = min(res, d1, d2)
        print(res)


def __starting_point():
    resolve()

__starting_point()
