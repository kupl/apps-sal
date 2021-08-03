from collections import deque
n = int(input())
g = [[] for _ in range(n)]
for i in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append([v, w])
    g[v].append([u, w])
used = [0] * n
used[0] = 1
parity = [-1] * n
parity[0] = 0
que = deque()
que.append(0)
while que:
    # print(que)
    v = que.popleft()
    for nv, w in g[v]:
        if used[nv]:
            continue
        parity[nv] = (parity[v] + w) % 2
        used[nv] = 1
        que.append(nv)

# print(used)
for i in range(n):
    print(parity[i])
