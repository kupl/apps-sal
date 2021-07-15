import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
def input():
    return sys.stdin.readline()[:-1]

def dfs(s):
    stack = [s]
    visited = [False]*N
    while stack:
        v = stack.pop()
        if visited[v]:
            continue
        visited[v] = True
        for u in graph[v]:
            if not visited[u]:
                point[u] += point[v]
                stack.append(u)

N, Q = list(map(int,input().split()))
graph = [deque([]) for _ in range(N)]
point = [0]*N

for i in range(N-1):
    a,b = list(map(int,input().split()))
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for i in range(Q):
    p,x = list(map(int,input().split()))
    p -= 1
    point[p] += x

dfs(0)
print((*point))

