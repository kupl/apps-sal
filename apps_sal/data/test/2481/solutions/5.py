from networkx import *
h, w = map(int, input().split())
G = DiGraph()
G.add_nodes_from(range(10))
C = [[*map(int, input().split())]for _ in "_" * 10]
G.add_weighted_edges_from([(i, j, C[i][j])for i in range(10)for j in range(10)])
S = [single_source_dijkstra_path_length(G, i)[1]for i in range(10)]
A = [[*map(int, input().split())]for _ in "_" * h]
print(sum(S[abs(x)] for a in A for x in a))
