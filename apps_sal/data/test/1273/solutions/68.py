from collections import deque

N = int(input())
G = [{} for i in range(N + 1)]
colors = []
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a][b] = [i, -1]
    G[b][a] = [i, -1]


def bfs(s):
    seen = [0 for i in range(N + 1)]
    prev = [0 for i in range(N + 1)]
    todo = deque([])
    cmax = 0
    now = s
    seen[now] = 1
    todo.append(now)
    while 1:
        if len(todo) == 0:
            break
        a = todo.popleft()
        if len(G[a]) < 50:
            if prev[a] == 0:
                a_color = set([])
            else:
                a_color = set([G[a][prev[a]][1]])
            for b in G[a]:
                if seen[b] == 0:
                    seen[b] = 1
                    todo.append(b)
                    prev[b] = a
                    for c in range(1, N + 1):
                        if c not in a_color:
                            a_color.add(c)
                            colors.append((G[a][b][0], c))
                            G[a][b][1] = G[b][a][1] = c
                            if c > cmax:
                                cmax = c
                            break
        else:
            temp = list(range(1, N))
            if prev[a] != 0:
                del temp[G[a][prev[a]][1] - 1]
            temp = deque(temp)
            for i, b in enumerate(G[a]):
                if seen[b] == 0:
                    seen[b] = 1
                    todo.append(b)
                    prev[b] = a
                    c = temp.popleft()
                    colors.append((G[a][b][0], c))
                    G[a][b][1] = G[b][a][1] = c
                    if c > cmax:
                        cmax = c

    return colors, cmax


colors, cmax = bfs(1)
colors = sorted(colors)

print(cmax)
for i in range(N - 1):
    print(colors[i][1])
