import sys
input = sys.stdin.readline

def bellmanford(G, s):
    n = len(G)
    inf = -float('inf')
    dist = [inf] * n
    dist[s] = 0
    for i in range(n):
        for v in range(n):
            for w, c in G[v]:
                if dist[w] < dist[v] + c:
                    dist[w] = dist[v] + c
                    if i >= n - 1 and w == n - 1:
                        return -1
    return dist

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append((b, c))
    dist = bellmanford(graph, 0)
    if dist == -1:
        print("inf")
    else:
        print(dist[N-1])

def __starting_point():
    main()
__starting_point()
