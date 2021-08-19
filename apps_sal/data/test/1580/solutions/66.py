from collections import defaultdict
import sys
import itertools
import time
import math
sys.setrecursionlimit(10 ** 7)
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
(N, M) = map(int, readline().split())
adj = [[] for _ in range(N)]
for i in range(M):
    (x, y, z) = map(int, readline().split())
    x -= 1
    y -= 1
    adj[x].append(y)
    adj[y].append(x)
visited = [False for _ in range(N)]


def dfs(v):
    if visited[v]:
        return False
    visited[v] = True
    for u in adj[v]:
        dfs(u)
    return True


ans = 0
for i in range(N):
    if dfs(i):
        ans += 1
print(ans)
