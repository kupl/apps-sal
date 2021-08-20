import sys
from bisect import bisect_left
input = sys.stdin.readline


def solve(Q, S, T, X):
    ans = [0] * Q
    INF = 10 ** 11
    for (q, x) in enumerate(X):
        min_dist = INF
        i_s = bisect_left(S, x)
        i_t = bisect_left(T, x)
        for s in (S[i_s - 1], S[i_s]):
            for t in (T[i_t - 1], T[i_t]):
                dist_s2t = abs(x - s) + abs(s - t)
                dist_t2s = abs(x - t) + abs(t - s)
                min_dist = min(min_dist, dist_s2t, dist_t2s)
        ans[q] = min_dist
    return ans


def main():
    (A, B, Q) = list(map(int, input().split()))
    S = [0] * (A + 2)
    T = [0] * (B + 2)
    X = [0] * Q
    for i in range(1, A + 1):
        S[i] = int(input())
    for i in range(1, B + 1):
        T[i] = int(input())
    for i in range(Q):
        X[i] = int(input())
    S[0] = T[0] = -10 ** 11
    S[-1] = T[-1] = 10 ** 11
    ans = solve(Q, S, T, X)
    print('\n'.join(map(str, ans)))


def __starting_point():
    main()


__starting_point()
