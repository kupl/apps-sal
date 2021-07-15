from collections import deque
n, m, d = map(int, input().split())
g = [[] for i in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

def bfs(init, c, p=False):
    nonlocal color
    q = deque(init)
    while len(q) > 0:
        u = q.popleft()
        for v in g[u]:
            if color[v] < 0:
                if p:
                    print(u, v)
                q.append(v)
                color[v] = c

color = [-1 for i in range(n + 1)]
color[1] = 0

c = 0
for x in g[1]:
    if color[x] < 0:
        color[x] = c
        bfs([x], c)
        c += 1

if len(g[1]) < d or d < c:
    print('NO')
else: 
    is_kid = [False for x in g[1]]
    kids = []
    
    picked = [False for i in range(c)]
    for i in range(len(g[1])):
        x = g[1][i]
        if not picked[color[x]]:
            is_kid[i] = True
            kids.append(x)
            picked[color[x]] = True

    extra = d - c
    for i in range(len(g[1])):
        x = g[1][i]
        if extra == 0:
            break
        if not is_kid[i]:
            is_kid[i] = True
            kids.append(x)
            extra -= 1

    color = [-1 for i in range(n + 1)]
    color[1] = 0

    print('YES')
    for x in kids:
        print(1, x)
        color[x] = 0

    bfs(kids, 0, True)
