import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
from collections import Counter
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
N = int(input())
adj = [[] for _ in range(N)]
for i in range(N - 1):
    a, b, c = list(map(int, input().split()))
    a -= 1
    b -= 1
    adj[a].append((c, b))
    adj[b].append((c, a))

Q, K = list(map(int, input().split()))
K -= 1

def dijkstra(start):
    dist = [INF for _ in range(N)]
    visited = [False for _ in range(N)] 
    q = [(0, start)]
    dist[start] = 0
    while len(q) > 0:
        v = heapq.heappop(q)
        a = v[1]
        if visited[a]:
            continue
        visited[a] = True
        for u in adj[a]:
            w = u[0]
            b = u[1]
            if dist[a] + w < dist[b]: 
                dist[b] = dist[a] + w
                heapq.heappush(q, (dist[b], b))
    return dist

dist = dijkstra(K)

for i in range(Q):
    x, y = list(map(int, input().split()))
    x -= 1
    y -= 1
    print((dist[x] + dist[y]))

