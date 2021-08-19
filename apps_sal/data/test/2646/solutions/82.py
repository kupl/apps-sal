from collections import deque
(n, m) = map(int, input().split())
l = [[] for i in range(n + 1)]
for i in range(m):
    (a, b) = map(int, input().split())
    l[a].append(b)
    l[b].append(a)
d = [-1] * (n + 1)
(d[0], d[1]) = (0, 0)
queue = deque()
queue.append(1)
while queue:
    x = queue.popleft()
    for i in l[x]:
        if d[i] == -1:
            d[i] = x
            queue.append(i)
print('Yes')
for i in d[2:]:
    print(i)
