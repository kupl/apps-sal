from collections import deque
import sys
input = sys.stdin.readline
(N, u, v) = map(int, input().split())
E = [tuple(map(int, input().split())) for i in range(N - 1)]
EDGE = [[] for i in range(N + 1)]
for (x, y) in E:
    EDGE[x].append(y)
    EDGE[y].append(x)
T = [-1] * (N + 1)
Q = deque()
Q.append(u)
T[u] = 0
while Q:
    x = Q.pop()
    for to in EDGE[x]:
        if T[to] == -1:
            T[to] = T[x] + 1
            Q.append(to)
A = [-1] * (N + 1)
Q = deque()
Q.append(v)
A[v] = 0
while Q:
    x = Q.pop()
    for to in EDGE[x]:
        if A[to] == -1:
            A[to] = A[x] + 1
            Q.append(to)
OK = [0] * (N + 1)
for i in range(N + 1):
    if T[i] < A[i]:
        OK[i] = 1
ANS = 0
for i in range(N + 1):
    if OK[i] == 1:
        ANS = max(ANS, A[i])
print(max(0, ANS - 1))
