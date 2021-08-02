import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
c = []
for i in range(3):
    c.append(list(map(int, input().split())))
graph = {}
for i in range(1, n + 1):
    graph[i] = []
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n + 1):
    if len(graph[i]) > 2:
        print(-1)
        break
    if len(graph[i]) == 1:
        root = i
else:
    ls = [root, graph[root][0]]
    root = graph[root][0]
    while len(ls) != n:
        for i in graph[root]:
            if i != ls[-2]:
                ls.append(i)
                root = i
                break
    perm = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    for lis in perm:
        N = n - len(lis)
        for i in range(N):
            lis.append(lis[i % 3])
    cost = []
    for lis in perm:
        temp = 0
        for i in range(n):
            temp += c[lis[i] - 1][ls[i] - 1]
        cost.append(temp)
    m = min(cost)
    print(m)
    for i in range(6):
        if cost[i] == m:
            ls = {ls[j]: perm[i][j] for j in range(n)}
            for i in range(1, n + 1):
                print(ls[i], end=' ')
            print()
            break
