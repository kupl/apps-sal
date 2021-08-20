import collections
(n, m) = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(m):
    (u, v) = map(int, input().split())
    graph[u].append(v)
flag = [False for i in range(n + 1)]
(s, t) = map(int, input().split())
queue = collections.deque([s])
count = 0
while True:
    for i in range(2):
        temp = set()
        while queue:
            test = queue.popleft()
            for j in graph[test]:
                if j not in temp:
                    temp.add(j)
        for j in temp:
            queue.append(j)
    temp = set()
    while queue:
        test = queue.popleft()
        for i in graph[test]:
            if flag[i] == True:
                continue
            elif i not in temp:
                temp.add(i)
                flag[i] = True
    count += 1
    if flag[t] == True:
        print(count)
        break
    if len(temp) == 0:
        print(-1)
        break
    for i in temp:
        queue.append(i)
