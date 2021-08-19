import sys
readline = sys.stdin.readline
(N, u, v) = list(map(int, readline().split()))
G = [[] for i in range(N)]
for i in range(N - 1):
    (a, b) = list(map(int, readline().split()))
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
dist_from_u = [0 for i in range(N)]
dist_from_v = [0 for i in range(N)]
stack = []
stack.append([u - 1, 0, -1])
while stack:
    (e, dist, parent) = stack.pop()
    dist_from_u[e] = dist
    for child in G[e]:
        if child == parent:
            continue
        stack.append([child, dist + 1, e])
stack = []
stack.append([v - 1, 0, -1])
while stack:
    (e, dist, parent) = stack.pop()
    dist_from_v[e] = dist
    for child in G[e]:
        if child == parent:
            continue
        stack.append([child, dist + 1, e])
maxdiff_from_v = 0
for i in range(N):
    if dist_from_u[i] < dist_from_v[i]:
        if maxdiff_from_v < dist_from_v[i]:
            maxdiff_from_v = dist_from_v[i]
print(maxdiff_from_v - 1)
