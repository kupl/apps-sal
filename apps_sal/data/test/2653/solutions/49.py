from collections import deque
import numpy as np

N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N - 1)]
P = [list(map(int, input().split())) for _ in range(Q)]

link = [[] for _ in range(N)]
for i in range(N - 1):
    link[A[i][0] - 1].append(A[i][1] - 1)
    link[A[i][1] - 1].append(A[i][0] - 1)


ans = [0 for _ in range(N)]
for i in range(Q):
    ans[P[i][0] - 1] += P[i][1]

dist = [-1 for _ in range(N)]
dist[0] = 0
d = deque([0])
while d:
    now = d.pop()
    for i in range(len(link[now])):
        if dist[link[now][i]] == -1:
            ans[link[now][i]] += ans[now]
            dist[link[now][i]] = 0
            d.append(link[now][i])

for i in range(N):
    if i != N - 1:
        print(ans[i], end=" ")
    else:
        print(ans[i])
