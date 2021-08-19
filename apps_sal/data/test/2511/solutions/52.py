import networkx as nx


def int1(x):
    return int(x) - 1


MOD = 10 ** 9 + 7
(N, K) = list(map(int, input().split()))
G = nx.Graph()
G.add_nodes_from(list(range(N)))
G.add_edges_from([tuple(map(int1, input().split())) for _ in range(N - 1)])
ans = K
for i in range(nx.degree(G)[0]):
    ans = ans * (K - i - 1) % MOD
for (parent, child) in nx.dfs_edges(G, 0):
    for i in range(nx.degree(G)[child] - 1):
        ans = ans * (K - i - 2) % MOD
print(ans)
