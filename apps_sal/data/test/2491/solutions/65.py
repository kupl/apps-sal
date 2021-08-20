import sys
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    pass


def __starting_point():
    main()


def bellman_ford(edges, N, start, goal):
    dist = [float('inf') for _ in range(N)]
    dist[start] = 0
    for i in range(N * 2):
        for (fro, to, cost) in edges:
            if dist[to] > dist[fro] + cost:
                dist[to] = dist[fro] + cost
                if i == N - 1:
                    dist[to] = -float('inf')
    return -dist[goal]


(N, M) = list(map(int, input().split()))
edges = []
for _ in range(M):
    (a, b, c) = list(map(int, input().split()))
    edges.append((a - 1, b - 1, -c))
cost = [float('inf') for _ in range(N)]
start = 0
goal = N - 1
ans = bellman_ford(edges, N, start, goal)
if ans == float('inf'):
    print(ans)
else:
    print(ans)
__starting_point()
