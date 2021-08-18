"""
Created on Mon Sep  7 21:29:58 2020

@author: liang
"""

from collections import deque
N, M = map(int, input().split())
adj = [list() for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

visited = [False for i in range(N)]
sign = [-1] * N


visited[0] = True
q = deque()
q.append(0)
sign[0] = 0

while q:
    cur = q.popleft()
    for a in adj[cur]:
        if not visited[a]:
            visited[a] = True
            sign[a] = cur + 1
            q.append(a)

if all(x >= 0 for x in sign):
    print("Yes")
    [print(a) for a in sign[1:]]
else:
    print("No")
