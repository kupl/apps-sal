from networkx import *
(n, m) = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
g = Graph(a)
ans = 0
for x in a:
    g.remove_edges_from([x])
    if not is_connected(g):
        ans += 1
    g.add_edges_from([x])
print(ans)
