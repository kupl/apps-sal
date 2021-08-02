#!/usr/bin/env python3

import networkx as nx


n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
cd = [list(map(int, input().split())) for i in range(n)]


match_list = [[] for i in range(n)]
for i in range(n):
    for j in range(n):
        a, b = ab[i]
        c, d = cd[j]

        if a < c and b < d:
            match_list[i].append(j)
# print(match_list)


group1 = list(range(n))
group2 = list(range(n, 2 * n))

g = nx.Graph()
g.add_nodes_from(group1, bipartite=1)
g.add_nodes_from(group2, bipartite=0)

for i, list_ in enumerate(match_list):
    for j in list_:
        g.add_edge(i, j + n, weight=1)

# A, B = bipartite.sets(g)
# print(A, B)
# pos = dict()
# pos.update((n, (1, i)) for i, n in enumerate(A))
# pos.update((n, (2, i)) for i, n in enumerate(B))
# nx.draw_networkx(g, pos)
# nx.draw_networkx_edges(g, pos)
# plt.axis("off")
# plt.show()


d = nx.max_weight_matching(g)

print((len(d)))
