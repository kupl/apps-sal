from collections import deque
(n, u, v) = map(int, input().split())
tree = [[] for _ in range(n)]
for i in range(n - 1):
    (a, b) = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)
not_yet = deque([u - 1])
already = [False] * n
already[u - 1] = True
dist = [0] * n
while not_yet:
    key = not_yet.popleft()
    for value in tree[key]:
        if already[value]:
            continue
        dist[value] = dist[key] + 1
        already[value] = True
        not_yet.append(value)
not_yet = deque([v - 1])
already = [False] * n
already[v - 1] = True
dist2 = [0] * n
while not_yet:
    key = not_yet.popleft()
    for value in tree[key]:
        if already[value]:
            continue
        dist2[value] = dist2[key] + 1
        already[value] = True
        not_yet.append(value)
judge = dist[v - 1]
ans = 0
for i in range(n):
    if dist[i] + dist2[i] > judge:
        if dist[i] >= dist2[i]:
            continue
        sub = dist2[i] - 1
    else:
        sub = judge - 1
    if sub > ans:
        ans = sub
print(ans)
