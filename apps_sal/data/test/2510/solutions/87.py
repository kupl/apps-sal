import networkx as nx
(n, m) = map(int, input().split())
uf = nx.utils.UnionFind()
for _ in range(m):
    (a, b) = map(int, input().split())
    uf.union(a, b)
ans = 1
for i in uf.to_sets():
    ans = max(ans, len(i))
print(ans)
