import sys
from bisect import bisect_left
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    (A, B, Q) = list(map(int, readline().split()))
    S = [int(readline()) for _ in range(A)]
    T = [int(readline()) for _ in range(B)]
    X = [int(readline()) for _ in range(Q)]
    ans = [INF] * Q
    vs = [0] * 2
    vt = [0] * 2
    for (i, x) in enumerate(X):
        idx_s = bisect_left(S, x)
        idx_t = bisect_left(T, x)
        vs[0] = S[idx_s - 1] if idx_s > 0 else -INF
        vt[0] = T[idx_t - 1] if idx_t > 0 else -INF
        vs[1] = S[idx_s] if idx_s < A else INF
        vt[1] = T[idx_t] if idx_t < B else INF
        for s in vs:
            for t in vt:
                ans[i] = min(ans[i], abs(x - s) + abs(s - t), abs(x - t) + abs(t - s))
    print('\n'.join(map(str, ans)))
    return


def __starting_point():
    main()


__starting_point()
