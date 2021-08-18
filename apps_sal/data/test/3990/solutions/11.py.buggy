from collections import deque
[n, m] = [int(i) for i in input().split()]
routes = [set() for i in range(n + 1)]
for i in range(m):
    [x, y] = [int(j) for j in input().split()]
    routes[x].add(y)
    routes[y].add(x)
if n not in routes[1]:
    a = True
else:
    a = False
way = deque()
way.append(1)
b = [-1 for i in range(n + 1)]
b[1] = 0
while len(way) > 0:
    c = way.popleft()
    for i in range(1, n + 1):
        if a ^ (i in routes[c]):
            continue
        if b[i] == -1:
            b[i] = b[c] + 1
            way.append(i)
            if i == n:
                print(b[i])
                return
print(-1)
