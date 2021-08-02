import sys
readline = sys.stdin.readline

N, Q = map(int, readline().split())

G = [[] for i in range(N)]

for i in range(N - 1):
    a, b = map(int, readline().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

point = [0] * N
for i in range(Q):
    p, x = map(int, readline().split())
    point[p - 1] += x

stack = [(0, -1, 0)]
while stack:
    v, parent, p = stack.pop()
    point[v] += p
    p = point[v]
    for child in G[v]:
        if child == parent:
            continue
        stack.append([child, v, p])

print(*point)
