import numpy as np
import io
import math
from scipy.sparse.csgraph import shortest_path
(nim, mike) = map(int, input().split())
array = [[int(x) for x in input().split()] for _ in range(mike)]
graph = np.zeros((nim, nim))
for (a, b, c) in array:
    graph[a - 1, b - 1] = c
dist = shortest_path(graph, directed=False).astype(int)
answer = 0
for (a, b, c) in array:
    if c != dist[a - 1, b - 1]:
        answer += 1
print(answer)
