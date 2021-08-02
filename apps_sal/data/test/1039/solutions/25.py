import sys
readline = sys.stdin.readline

N = int(readline())
G = [[] for i in range(N)]

for i in range(N - 1):
    a, b, c = list(map(int, readline().split()))
    G[a - 1].append((b - 1, c))
    G[b - 1].append((a - 1, c))

Q, K = list(map(int, readline().split()))

dist = [0] * N
stack = [(K - 1, -1, 0)]
while stack:
    v, parent, cost = stack.pop()
    dist[v] = cost
    for child, c in G[v]:
        if child == parent:
            continue
        stack.append((child, v, cost + c))

for i in range(Q):
    x, y = list(map(int, readline().split()))
    print((dist[x - 1] + dist[y - 1]))
