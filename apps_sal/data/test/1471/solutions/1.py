from collections import deque

n = int(input())
tree = {i: set() for i in range(n)}
cost = {}
for _ in range(n - 1):
    u, v, w = [int(x) - 1 for x in input().split()]
    tree[u].add(v)
    tree[v].add(u)
    cost[(u, v)] = w + 1

color = [-1] * n
color[0] = 0
que = deque([0])
while que:
    now = que.popleft()
    for i in tree[now]:
        if color[i] != -1:
            continue
        if cost[(min(now, i), max(now, i))] % 2 == 0:
            color[i] = color[now]
        else:
            color[i] = color[now] ^ 1
        que.append(i)
print(('\n'.join(map(str, color))))
