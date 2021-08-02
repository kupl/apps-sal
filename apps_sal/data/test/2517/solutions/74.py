from scipy.sparse.csgraph import shortest_path
import numpy as np
import itertools

N, M, R = list(map(int, input().split()))
r = list(map(int, input().split()))

edge = np.zeros((N + 1, N + 1))
for _ in range(M):
    A, B, C = list(map(int, input().split()))
    edge[A, B] = C
dist = shortest_path(edge, directed=False).astype(int)

answer = 10**18
for visit in itertools.permutations(r):
    p = 0
    prev = visit[0]
    for x in visit[1:]:
        if prev != None:
            p += dist[prev, x]
        prev = x
    answer = min(answer, p)

print(answer)
