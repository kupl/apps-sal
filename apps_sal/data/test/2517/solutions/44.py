import heapq
import itertools
from collections import defaultdict
(n, m, r) = list(map(int, input().split()))
visiting_town = list(map(int, input().split()))
edges = [[] for i in range(n + 1)]
for _ in range(m):
    (_from, to, distance) = list(map(int, input().split()))
    edges[_from].append([to, distance])
    edges[to].append([_from, distance])
comp_edges = defaultdict(dict)
for _from in visiting_town:
    seen = [False] * (n + 1)
    todo = []
    for (to, dist) in edges[_from]:
        heapq.heappush(todo, [dist, to])
    while todo:
        (dist, node) = heapq.heappop(todo)
        if seen[node]:
            continue
        seen[node] = dist
        for (to, add_dist) in edges[node]:
            if seen[to] or to == _from:
                continue
            new_dist = dist + add_dist
            heapq.heappush(todo, [new_dist, to])
    for to in visiting_town:
        if to == _from:
            continue
        comp_edges[_from][to] = seen[to]
candidates = []
for route in itertools.permutations(visiting_town):
    result = 0
    for (_from, to) in zip(route[:-1], route[1:]):
        if to in comp_edges[_from]:
            dist = comp_edges[_from][to]
            result += dist
        else:
            break
    candidates.append(result)
print(min(candidates))
