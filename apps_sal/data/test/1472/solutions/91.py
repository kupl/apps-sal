#!/usr/bin/env python3
def main():
    from collections import deque
        
    N, X, Y = list(map(int, input().split()))

    G = [[1]] + [[x - 1, x + 1] for x in range(1, N - 1)] + [[N - 2]]
    G[X - 1].append(Y - 1)
    G[Y - 1].append(X - 1)

    dist = [[-1] * N for _ in [0] * N]
    for s in range(N):
        q = deque([s])
        dist[s][s] = 0
        while q:
            v = q.popleft()
            for nv in G[v]:
                if dist[s][nv] == -1:
                    dist[s][nv] = dist[s][v] + 1
                    q.append(nv)
    res = [0] * N
    for i in range(N):
        for j in range(i + 1, N):
            res[dist[i][j]] += 1
    for d in range(1, N):
        print((res[d]))


def __starting_point():
    main()

__starting_point()
