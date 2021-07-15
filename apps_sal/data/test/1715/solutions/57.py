import sys
from bisect import bisect_left

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A, B, Q = list(map(int, readline().split()))
    S = [-INF] + [int(readline()) for _ in range(A)] + [INF]
    T = [-INF] + [int(readline()) for _ in range(B)] + [INF]
    X = [int(readline()) for _ in range(Q)]

    ans = [INF] * Q
    for i, x in enumerate(X):
        idx_s = bisect_left(S, x)
        idx_t = bisect_left(T, x)

        for s in (S[idx_s - 1], S[idx_s]):
            for t in (T[idx_t - 1], T[idx_t]):
                ans[i] = min(ans[i], abs(x - s) + abs(s - t), abs(x - t) + abs(t - s))

    print(('\n'.join(map(str, ans))))

    return


def __starting_point():
    main()

__starting_point()
