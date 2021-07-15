#!/usr/bin/env python3
from collections import deque

def main():
    N, u, v = map(int, input().split())
    s = u-1
    t = v-1
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(lambda x: int(x)-1, input().split())
        adj[a].append(b)
        adj[b].append(a)
    
    # aoki BFS
    queue = deque([t])
    visit = [-1] * N
    visit[t] = 0
    
    while queue:
        now = queue.popleft()
        for u in adj[now]:
            if visit[u] < 0:
                queue.append(u)
                visit[u] = visit[now] + 1
                # parent[u] = now

    # takahashi BFS
    queue = deque([s])
    visit2 = [-1] * N
    # parent = [-1] * N
    visit2[s] = 0
    
    
    while queue:
        now = queue.popleft()
        for u in adj[now]:
            if visit2[u] < 0:
                queue.append(u)
                visit2[u] = visit2[now] + 1

    ans = [-1,-1]
    # print(visit, visit2)
    for i in range(N):
        if visit[i] >= visit2[i] and visit[i] > ans[0]:
            ans = [visit[i], i]
    
    print(visit[ans[1]]-1)

def __starting_point():
    main()
__starting_point()
