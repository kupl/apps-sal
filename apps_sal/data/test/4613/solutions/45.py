# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 00:49:45 2020

@author: liang
"""
from collections import deque

def isBridge(start, goal):
    visited = [False]*N
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        cur = q.popleft()
        if cur == goal:
            return False
        for nex in adj[cur]:
            if not visited[nex]:
                visited[nex] = True
                q.append(nex)
    return True     

N, M = map(int, input().split())
adj = list()


for i in range(N):
    adj.append(list())

E = list()
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    E.append((a,b))
    adj[a].append(b)
    adj[b].append(a)
ans = 0
for e in E:
    a, b = e
    adj[a].remove(b)
    adj[b].remove(a)
    if isBridge(a,b):
        ans += 1
    adj[a].append(b)
    adj[b].append(a)
print(ans)
