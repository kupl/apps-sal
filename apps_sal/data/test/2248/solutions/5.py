import copy
import sys
import threading

threading.stack_size(64 * 1024 * 1024)
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())

ans = 0
sz = [0] * (n + 1)
graph = []

for _ in range(n + 1):
    graph.append([])

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v, pr):
    nonlocal ans
    for to in graph[v]:
        if to != pr:
            dfs(to, v)
    if pr != -1:
        ans = max(ans, sz[pr] + sz[v])
        sz[pr] = max(sz[pr], sz[v] + 1)

def main():
    dfs(1, -1)
    print(ans + 1)
    
th = threading.Thread(target=main)
th.start()
