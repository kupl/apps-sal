import collections

n, u, v = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
q = collections.deque()
q.append((v, 0))
checked = [0] * (n + 1)
dist1 = [0] * (n + 1)
while len(q) != 0:
    tv, td = q.popleft()
    checked[tv] = 1
    dist1[tv] = td
    for tu in g[tv]:
        if checked[tu] == 1:
            continue
        q.append((tu, td + 1))
q = collections.deque()
q.append((u, 0))
checked = [0] * (n + 1)
dist2 = [0] * (n + 1)
while len(q) != 0:
    tv, td = q.popleft()
    checked[tv] = 1
    dist2[tv] = td
    for tu in g[tv]:
        if checked[tu] == 1:
            continue
        q.append((tu, td + 1))
ans = 0
for tv in range(1, n + 1):
    if dist1[tv] > dist2[tv]:
        ans = max(ans, dist1[tv] - 1)
print(ans)
