import sys


def find_farest_v(v, g):
    queue_v = [(v, 0)]
    order = []
    visited_v = set()
    while queue_v:
        current_v, dist = queue_v.pop(0)
        visited_v.add(current_v)
        order.append((current_v, dist))
        for neib in adj_graph[current_v]:
            if neib not in visited_v:
                queue_v.append((neib, dist + 1))

    return order[-1]


n, m = list(map(int, input().strip().split(" ")))

adj_graph = [[] for i in range(n)]

for i in range(m):
    line = input()
    v1, v2 = list(map(int, line.split(" ")))
    adj_graph[v1 - 1].append(v2 - 1)
    adj_graph[v2 - 1].append(v1 - 1)

v1, d1 = find_farest_v(0, adj_graph)
v2, d2 = find_farest_v(v1, adj_graph)

print(d2)
