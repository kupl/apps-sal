import sys
sys.setrecursionlimit(10 ** 7)


def main():
    (N, M) = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        (a, b, c) = list(map(int, input().split()))
        G[a - 1].append((b - 1, c))
    INF = 10 ** 40
    S = [-INF] * N
    S[0] = 0

    def helper(n, s, hist):
        for (g, gc) in G[n]:
            if S[g] >= s + gc or S[g] >= INF:
                continue
            S[g] = s + gc
            if g in hist:
                S[g] = INF
            hist[g] = hist.get(g, 0) + 1
            helper(g, S[g], hist)
            hist[g] -= 1
            if hist[g] == 0:
                del hist[g]
    helper(0, 0, {0: 1})
    s = S[-1]
    return s if s < INF else 'inf'


print(main())
