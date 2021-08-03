
from copy import copy
N = int(input())
G = [[] for _ in range(N)]
di = [-1] * N
for i in range(N - 1):
    u, v, w = map(int, input().split())
    G[u - 1].append([v - 1, w])
    G[v - 1].append([u - 1, w])

di[0] = 0

for i in range(1, N):
    if di[i] != -1:
        continue
    seen = [0] * N
    stack = [[0, 0]]
    while stack:
        y, d = stack.pop()
        if seen[y] == 1:
            continue
        seen[y] = 1
        for z, dist in G[y]:
            if seen[z] == 0:
                di[z] = d + dist
                stack.append([z, d + dist])

for i in range(N):
    if di[i] % 2 == 0:
        print(0)
    else:
        print(1)
