#coding: utf-8
from collections import defaultdict, deque

N = int(input())
G = {}
for i in range(1, N+1):
    G[i] = []

for i in range(N-1):
    u, v, w = (int(n) for n in input().split())
    G[u].append((v, w))
    G[v].append((u, w))

ret = [-1] * (N+1)

que = deque()
que.append((1, 0))

while len(que) > 0:
    node, distance = que[0]
    que.popleft()

    ret[node] = distance % 2
    for next_node, next_distance in G[node]:
        if ret[next_node] == -1:
            que.append((next_node, distance + next_distance))

for i in range(N):
    print((ret[i+1]))


