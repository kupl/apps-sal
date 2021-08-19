from collections import deque
n = int(input())
uvw = [list(map(int, input().split())) for _ in range(n - 1)]
l = [[] for _ in range(n)]
for (u, v, w) in uvw:
    (u, v) = (u - 1, v - 1)
    l[u].append((v, w))
    l[v].append((u, w))
ans = [0] * n
parents = [-1] * n
q = deque([0])
while q:
    a = q.pop()
    for (i, j) in l[a]:
        if i == parents[a]:
            continue
        parents[i] = a
        q.append(i)
        ans[i] = ans[a] if j % 2 == 0 else (ans[a] + 1) % 2
for i in ans:
    print(i)
