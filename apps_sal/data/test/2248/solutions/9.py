# https://www.youtube.com/watch?v=_q7aMi-5Uos
import sys
from collections import defaultdict

n, m = list(map(int, sys.stdin.readline().lstrip().rstrip().split()))
graph = defaultdict(list)
for i in range(m):
    u, v = list(map(int, sys.stdin.readline().lstrip().rstrip().split()))
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

visited = [False for i in range(n)]
q = [[0, 0]]
temp = []
visited[0] = True
while q != []:
    node, dist = q[0][0], q[0][1]
    q.pop(0)
    leaf = True
    for v in graph[node]:
        if visited[v] == False:
            visited[v] = True
            q.append([v, dist + 1])
            leaf = False
    if leaf:
        temp.append([dist, node])
temp.sort()

visited = [False for i in range(n)]
q = [[temp[-1][1], 0]]
temp = []
visited[q[0][0]] = True
while q != []:
    node, dist = q[0][0], q[0][1]
    q.pop(0)
    leaf = True
    for v in graph[node]:
        if visited[v] == False:
            visited[v] = True
            q.append([v, dist + 1])
            leaf = False
    if leaf:
        temp.append(dist)
sys.stdout.write(str(max(temp)) + '\n')
