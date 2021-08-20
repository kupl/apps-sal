from heapq import heappop, heappush
from copy import deepcopy


def main():
    (N, M) = map(int, input().split())
    INF = 10 ** 9
    to = [[INF] * N for _ in range(N)]
    edges = []
    for _ in range(M):
        (a, b, c) = map(int, input().split())
        a -= 1
        b -= 1
        to[a][b] = c
        to[b][a] = c
        edges.append((a, b, c))
    for i in range(N):
        to[i][i] = 0

    def floyd_warshall():
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    to[i][j] = min(to[i][j], to[i][k] + to[k][j])
    floyd_warshall()
    ans = 0
    for (a, b, c) in edges:
        if to[a][b] != c:
            ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
