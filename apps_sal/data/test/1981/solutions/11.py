import queue
from sys import stdin


def param(x, y):
    if y == 0:
        return y
    return x


def bfs():
    nonlocal ans
    q = queue.Queue()
    dist[0] = cats[0]
    q.put(1)
    while not q.empty():
        curr = q.get()
        cats[curr - 1] = -1
        if dist[curr - 1] > limit:
            continue
        if len(graph[curr]) == 1 and curr != 1:
            ans += 1
        for neighbor in graph[curr]:
            if cats[neighbor - 1] != -1:
                dist[neighbor - 1] = param(dist[curr - 1] + cats[neighbor - 1], cats[neighbor - 1])
                q.put(neighbor)


live = True
if not live:
    stdin = open('data.in', 'r')

n, limit = list(map(int, stdin.readline().strip().split()))
cats = list(map(int, stdin.readline().strip().split()))
dist = [0] * n
graph = {}
for it in range(1, n):
    x, y = list(map(int, stdin.readline().strip().split()))
    if graph.get(x) == None:
        graph[x] = []
    graph[x] += [y]
    if graph.get(y) == None:
        graph[y] = []
    graph[y] += [x]

ans = 0
bfs()
print(ans)

if not live:
    stdin.close()
