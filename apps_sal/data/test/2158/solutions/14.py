from collections import defaultdict

graph = defaultdict(list)
d = {}
n = int(input())
for i in range(n - 1):
    u, v, cost = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)
    x = str(u) + ':' + str(v)
    y = str(v) + ':' + str(u)
    d[x] = cost
    d[y] = cost

q = [[0, 0]]
ans = []
visited = [False for i in range(n)]
visited[0] = True
while q != []:
    node, cost = q[0][0], q[0][1]
    q.pop(0)
    leaf = True
    for v in graph[node]:
        if visited[v] == False:
            visited[v] = True
            leaf = False
            x = str(node) + ':' + str(v)
            y = str(v) + ':' + str(node)
            if x in d:
                c = d[x]
            else:
                c = d[y]
            q.append([v, cost + c])
    if leaf:
        ans.append(cost)
print(max(ans))
