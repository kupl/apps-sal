import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, M = map(int, readline().split())
    W = list(map(int, readline().split()))
    w_max = max(W)

    mat = []
    for _ in range(M):
        l, v = map(int, readline().split())
        if v < w_max:
            return print(-1)
        mat.append((l, v))
    from operator import itemgetter

    mat.sort(key=itemgetter(0), reverse=True)
    mat.sort(key=itemgetter(1))

    L = [0]
    V = [0]
    m = 0

    for i in range(M):
        l, v = mat[i]
        m = max(m, l)
        L.append(m)
        V.append(v)

    from itertools import permutations
    import bisect
    ans = INF
    for per in permutations(range(N)):
        a = [W[i] for i in per]
        b = [[0] * N for _ in range(N)]
        for i in range(N - 1):
            cur = a[i]
            for j in range(i + 1, N):
                cur += a[j]
                p = bisect.bisect_left(V, cur)
                b[i][j] = L[p - 1]
        dp = [0] * N
        for i in range(N - 1):
            cur = dp[i]
            for j in range(i + 1, N):
                dp[j] = max(dp[j], cur + b[i][j])
        ans = min(ans, dp[N - 1])
    print(ans)


def __starting_point():
    main()


__starting_point()
