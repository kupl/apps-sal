from collections import deque
from sys import stdin


def BFS(s):
    if s == 0:
        distance = distance_Alice
    else:
        distance = distance_Bob
    distance[s] = 0
    q = deque()
    q.append(s)
    while len(q) > 0:
        v = q.popleft()
        for u in adjacents_list[v]:
            if distance[u] == -1:
                distance[u] = distance[v] + 1
                q.append(u)


(n, x) = map(int, stdin.readline().split())
distance_Alice = [-1 for i in range(n)]
distance_Bob = [-1 for i in range(n)]
adjacents_list = [[] for i in range(n)]
for i in range(n - 1):
    (v1, v2) = map(int, stdin.readline().split())
    adjacents_list[v1 - 1].append(v2 - 1)
    adjacents_list[v2 - 1].append(v1 - 1)
BFS(0)
BFS(x - 1)
max = 0
for i in range(n):
    if max < distance_Alice[i] and distance_Bob[i] < distance_Alice[i]:
        max = distance_Alice[i]
print(max * 2)
