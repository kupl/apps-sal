import sys


def input():
    return sys.stdin.readline().strip()


def bellman_ford(edges, N, start):
    dist = [float('inf') for _ in range(N)]
    dist[start] = 0
    for i in range(2 * N):
        for (fro, to, cost) in edges:
            if dist[to] > dist[fro] - cost:
                dist[to] = dist[fro] - cost
                if i == N - 1:
                    dist[to] = -float('inf')
    return dist


def main():
    (N, M) = list(map(int, input().split()))
    edge = []
    for i in range(M):
        (a, b, c) = list(map(int, input().split()))
        edge.append((a - 1, b - 1, c))
    D = bellman_ford(edge, N, 0)
    print(-1 * D[-1])


def __starting_point():
    main()


__starting_point()
