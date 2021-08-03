from collections import deque
n, m = map(int, input().split())
dis = [n + 2] * (n)
dis[0] = 0
near = [[] for _ in range(n)]
mark = [-1] * (n)
mark[0] = 0
que = deque()
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    near[a].append(b)
    near[b].append(a)
    if a == 0:
        que.appendleft(b)
        mark[b] = 0
        dis[b] = 1
    if b == 0:
        que.appendleft(a)
        mark[a] = 0
        dis[a] = 1
while que:
    i = que.popleft()
    for j in near[i]:
        if dis[i] + 1 < dis[j]:
            dis[j] = dis[i] + 1
            mark[j] = i
            que.append(j)
if n + 2 not in dis:
    print('Yes')
    for i in mark[1:]:
        print(i + 1)
else:
    print('No')
