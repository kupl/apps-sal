import networkx as nx

N = int(input())
ABC = [list(map(int, input().split())) for _ in range(N - 1)]
Q, K = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(Q)]

G = nx.Graph()

for a, b, c in ABC:
    G.add_edge(a - 1, b - 1, weight=c)

pred, dist = nx.dijkstra_predecessor_and_distance(G, K - 1)

for x, y in XY:
    print((dist[x - 1] + dist[y - 1]))


