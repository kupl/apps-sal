from networkx import *
N = int(input())
E1 = [list(map(int, input().split())) for n in range(N - 1)]
(Q, K) = map(int, input().split())
E2 = [list(map(int, input().split())) for q in range(Q)]
G = Graph()
for (a, b, c) in E1:
    G.add_edge(a - 1, b - 1, weight=c)
D = shortest_path_length(G, weight='weight', target=K - 1)
for (x, y) in E2:
    print(D[x - 1] + D[y - 1])
