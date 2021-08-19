from collections import deque
N = int(input())
V = set()
E = {}
for _ in range(N):
    (x, y) = map(int, input().split())
    y += 100010
    V.add(x)
    V.add(y)
    if x not in E:
        E[x] = [y]
    else:
        E[x].append(y)
    if y not in E:
        E[y] = [x]
    else:
        E[y].append(x)
visited = [False] * 200020
willSearch = [False] * 200020
Q = deque()
ans = 0
for v in V:
    if visited[v]:
        continue
    Q.append(v)
    (xcount, ycount) = (0, 0)
    edge_count = 0
    while len(Q) > 0:
        now = Q.pop()
        visited[now] = True
        if now > 100005:
            ycount += 1
        else:
            xcount += 1
        for nxt in E[now]:
            edge_count += 1
            if visited[nxt] or willSearch[nxt]:
                continue
            willSearch[nxt] = True
            Q.append(nxt)
    ans += xcount * ycount
    ans -= edge_count // 2
print(ans)
