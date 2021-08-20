from collections import defaultdict
__author__ = 'artyom'


def read():
    return map(int, input().split())


all_edges = defaultdict(list)
(n, m) = read()
for _ in range(m):
    (a, b, c) = read()
    all_edges[c].append((a, b))
graphs = []


def root(components, x, l=0):
    return (x, l) if components[x] == x else root(components, components[x], l + 1)


def connected_components(edges):
    components = [i for i in range(n + 1)]
    for (u, v) in edges:
        (ru, lu) = root(components, u)
        (rv, lv) = root(components, v)
        if ru != rv:
            if lu < lv:
                components[ru] = rv
            else:
                components[rv] = ru
    return components


for (c, edges) in all_edges.items():
    graphs.append(connected_components(edges))


def count_in_same_component(u, v):
    count = 0
    for graph in graphs:
        if root(graph, u)[0] == root(graph, v)[0]:
            count += 1
    return count


ans = ''
for __ in range(int(input())):
    (u, v) = read()
    ans += str(count_in_same_component(u, v)) + '\n'
print(ans)
