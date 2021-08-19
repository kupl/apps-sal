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
        # a,b=a-1,b-1
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    # def bfs(graph):
    q = deque([0])
    #level=[0 for i in range(len(graph))]
    parent = [-1] * len(graph)
    visit = []
    while q:
        v = q.popleft()
        visit.append(v)
        for adj in graph[v]:
            if adj != parent[v]:
                # level[adj]=level[v]+1
                parent[adj] = v
                q.append(adj)

        # return parent,visit

    # parent,visit=bfs(graph)
    # print(level,parent,visit)

    cur = X
    path = [X]
    # print(path,'path')
    while(parent[X] != -1):
        X = parent[X]
        path += [X]

    P = len(path) - 1

    toleft = parent
    # bfsvisit=visit[::-1]
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

    # print(path,toleft)
    # print(P,'P')
    MAX = 0

    for t in range(0, P + 1):
        if 2 * t < P:
            temp = 2 * t + (2 * toleft[path[t]] + 2 * abs(P - 2 * t))
            if temp > MAX:
                MAX = temp
        else:
            break

    print(MAX)

    # print(toleft[2],path)
main()
