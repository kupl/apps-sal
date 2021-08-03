import sys


N, M = list(map(int, input().split()))
edge = []
for s in sys.stdin.readlines():
    a, b, c = list(map(int, s.split()))
    edge.append((a - 1, b - 1, c))

path = [-float('inf')] * N
path[0] = 0

for i in range(N - 1):
    for j in range(M):
        a, b, c = edge[j]
        if path[b] < path[a] + c:
            path[b] = path[a] + c


for i in range(N - 1):
    for j in range(M):
        a, b, c = edge[j]
        if path[b] < path[a] + c:
            path[b] = float('inf')

print((path[-1]))
