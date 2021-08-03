import sys
visited = set()
success = 1
sys.setrecursionlimit(1000000)


def dfs(graph, node):
    nonlocal visited
    nonlocal b
    nonlocal success
    if node not in visited:
        visited.add(node)
        for counter in range(len(graph[node - 1][0])):
            if b[graph[node - 1][0][counter] - 1] == 10000000000000000000:
                b[graph[node - 1][0][counter] - 1] = b[node - 1] + graph[node - 1][1][counter]
            else:
                if b[graph[node - 1][0][counter] - 1] != b[node - 1] + graph[node - 1][1][counter]:
                    success = 0
            dfs(graph, graph[node - 1][0][counter])


n, m = map(int, input().split())
a = []
b = [10000000000000000000] * n
for i in range(n):
    a.append([[], []])
done = [0] * n
for i in range(m):
    l, r, d = map(int, input().split())
    a[l - 1][0].append(r)
    a[l - 1][1].append(d)
    a[r - 1][0].append(l)
    a[r - 1][1].append(-d)
current = [1]
for i in range(n):
    if i + 1 in visited:
        continue
    b[i] = 0
    dfs(a, i + 1)
if success == 0:
    print('No')
else:
    print('Yes')
