from collections import deque
(n, m) = list(map(int, input().split()))
a = []
rinsetu = [[] for i in range(n + 1)]
count = [0 for i in range(n + 1)]
for i in range(m):
    (u, v) = list(map(int, input().split()))
    count[u] += 1
    count[v] += 1
    a.append([u, v])
    rinsetu[u].append(v)
    rinsetu[v].append(u)
root = count.index(max(count))
visitflag = [0 for i in range(n + 1)]
queue = deque([root])
while len(queue) > 0:
    now = queue.popleft()
    for i in rinsetu[now]:
        if visitflag[i] == 0:
            visitflag[i] = now
            queue.append(i)
for i in range(1, n + 1):
    if i == root:
        continue
    else:
        print(i, visitflag[i])
