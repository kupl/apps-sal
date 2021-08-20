import numpy as np
from itertools import combinations
(h, w, k) = map(int, input().split())
graph = []
for i in range(h):
    row = [1 if x == '#' else 0 for x in input()]
    graph.append(row)
graph = np.array(graph)
h_combi = []
w_combi = []
for i in range(1, h + 1):
    h_combi.extend(list(combinations(range(h), i)))
for i in range(1, w + 1):
    w_combi.extend(list(combinations(range(w), i)))
ans = 0
for hi in h_combi:
    for wi in w_combi:
        cnt = 0
        for y in hi:
            if cnt > k:
                break
            for x in wi:
                cnt += graph[y][x]
        if cnt == k:
            ans += 1
print(ans)
