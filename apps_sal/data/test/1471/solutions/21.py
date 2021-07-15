import collections

n = int(input())
graph = [[] for i in range(n + 1)]
flag = [False for i in range(n + 1)]
for i in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
    graph[v].append([u, w])
color = [None for i in range(n + 1)]
color[1] = 0
queue = collections.deque([1])
while queue:
    test = queue.popleft()
    flag[test] = True
    for i in graph[test]:
        if flag[i[0]] == True:
            continue
        queue.append(i[0])
        color[i[0]] = i[1] % 2 ^ color[test]
for i in range(n):
    print(color[i + 1])
