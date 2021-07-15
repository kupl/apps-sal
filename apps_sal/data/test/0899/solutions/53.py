import networkx as nx
import itertools

N, M = map(int, input().split())
G = nx.Graph()
G.add_weighted_edges_from([map(int, input().split()) for _ in range(M)])
S = nx.floyd_warshall(G)

ans = M
for i, j, d in G.edges(data=True):
    for s, t in itertools.combinations(G.nodes(), 2):
        if S[s][i] + d['weight'] + S[j][t] == S[s][t]:
            ans -= 1
            break
print(ans)
