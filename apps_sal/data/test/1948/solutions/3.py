from sys import stdin, stderr
from collections import defaultdict, deque


def main():
    n, x = map(int, stdin.readline().strip().split())
    X = x - 1
    graph = [[] for i in range(n)]
    for i in range(n):
        graph[i] = []
    for _ in range(n - 1):
        a, b = map(int, stdin.readline().strip().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    q = deque([0])
    parent = [-1] * len(graph)
    visit = []
    while q:
        v = q.popleft()
        visit.append(v)
        for adj in graph[v]:
            if adj != parent[v]:
                parent[adj] = v
                q.append(adj)

    cur = X
    path = [X]
    while(parent[X] != -1):
        X = parent[X]
        path += [X]

    P = len(path) - 1

    toleft = parent
    for i in range(1, len(visit)):
        x = visit[-i]

        if [parent[x]] == graph[x]:
            toleft[x] = 0
        else:
            ans = 0
            for adj in graph[x]:
                if adj != parent[x]:
                    ans = max(toleft[adj], ans)
            ans += 1
            toleft[x] = ans

    MAX = 0

    for t in range(0, P + 1):
        if 2 * t < P:
            temp = 2 * t + (2 * toleft[path[t]] + 2 * abs(P - 2 * t))
            if temp > MAX:
                MAX = temp
        else:
            break

    print(MAX)


main()
