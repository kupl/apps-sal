import sys
import math
import collections
import itertools
input = sys.stdin.readline
N = int(input())
road = [[] for i in range(N + 1)]
for _ in range(N - 1):
    (u, v, w) = list(map(int, input().split()))
    road[u].append((v, w))
    road[v].append((u, w))
dist = [float('inf') for i in range(N + 1)]
ans = [0] * (N + 1)
q = collections.deque([])
q.append(1)
dist[1] = 0
while q:
    now = q.popleft()
    for (goto, cost) in road[now]:
        if dist[goto] > dist[now] + cost:
            dist[goto] = dist[now] + cost
            q.append(goto)
for a in dist[1:]:
    print(a % 2)
