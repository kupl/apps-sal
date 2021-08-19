try:
    from string_source import string_source
except ImportError:
    source = input
from collections import defaultdict


def complete_bipartite(n, edges):
    if not edges:
        return False
    neighbors = defaultdict(set, {})
    for (e1, e2) in edges:
        neighbors[e1].add(e2)
        neighbors[e2].add(e1)
    (s1, s2) = edges[0]
    groups = [None, None, None]
    groups[2] = neighbors[s1].intersection(neighbors[s2])
    groups[1] = neighbors[s1].difference(neighbors[s2])
    groups[0] = set(neighbors).difference(groups[2], groups[1])

    def get_group(node):
        return next((idx for (idx, g) in enumerate(groups) if node in g))
    sizes = [len(g) for g in groups]
    if sum((len(g) for g in groups)) < n:
        return False
    if any((len(g) == 0 for g in groups)):
        return False
    for (e1, e2) in edges:
        if get_group(e1) == get_group(e2):
            return False
    answer = [0] * n
    for (node, neigh) in list(neighbors.items()):
        g = get_group(node)
        if sum((s for (idx, s) in enumerate(sizes) if idx != g)) != len(neigh):
            return False
        answer[node - 1] = g + 1
    return answer


def answer(source):
    (n, m) = list(map(int, source().strip().split()))
    edges = [[int(k) for k in source().strip().split()] for _ in range(m)]
    a = complete_bipartite(n, edges)
    if not a:
        print(-1)
    else:
        print(' '.join(map(str, a)))


answer(input)
if False:
    answer(string_source('6 11\n    1 2\n    1 3\n    1 4\n    1 5\n    1 6\n    2 4\n    2 5\n    2 6\n    3 4\n    3 5\n    3 6'))
    answer(string_source('4 6\n    1 2\n    1 3\n    1 4\n    2 3\n    2 4\n    3 4'))
