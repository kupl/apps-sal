from collections import deque
(n, m) = map(int, input().split())
e = [[] for i in range(n)]
for i in range(m):
    (f, t) = map(int, input().split())
    f -= 1
    t -= 1
    e[f].append(t)
    e[t].append(f)
INF = 10 ** 9
dist = [INF] * n
dist[0] = 0
d = deque()
d.append([0, 0])
while d:
    (f, c) = d.pop()
    if c >= 2:
        break
    for t in e[f]:
        if c + 1 < dist[t]:
            dist[t] = c + 1
            d.appendleft([t, c + 1])
print('POSSIBLE') if dist[n - 1] <= 2 else print('IMPOSSIBLE')
