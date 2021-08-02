from collections import defaultdict, deque

n, m = list(map(int, input().split()))

state = list(map(int, input().split()))

graph = defaultdict(list)

connected = [list() for _ in range(n + 1)]  # Each node connected to which 2 edges
for i in range(m):
    for j in list(map(int, input().split()))[1:]:
        connected[j].append(i)

for index, i in enumerate(connected[1:]):
    graph[i[0]].append((i[1], state[index]))
    graph[i[1]].append((i[0], state[index]))

switch_color = [False] * m
switch_visited = [False] * m
# print(connected)
# print(graph)
queue = deque([])
yes = True
for nodes in graph:
    if yes and (not switch_visited[nodes]):
        # queue = deque([nodes])
        # yes = True
        queue.append(nodes)
        while queue and yes:
            now = queue.popleft()
            switch_visited[now] = True
            for i in graph[now]:
                if not switch_visited[i[0]]:
                    switch_visited[i[0]] = True
                    queue.append(i[0])
                    if i[1] == 1:
                        switch_color[i[0]] = switch_color[now]
                    else:
                        switch_color[i[0]] = (not switch_color[now])
                else:
                    if (i[1] == 1) and (switch_color[i[0]] != switch_color[now]):
                        print("NO")
                        yes = False
                        break
                    elif i[1] == 0 and switch_color[i[0]] == switch_color[now]:
                        print("NO")
                        yes = False
                        break
if yes:
    print("YES")
