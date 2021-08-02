from collections import deque
N, M = map(int, input().split())
g = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = [int(x) for x in input().split()]
    g[a].append(b)
    g[b].append(a)


queue = deque([1])
d = [None] * (N + 1)
d[1] = 0
ans = [0] * (N + 1)
while queue:
    v = queue.popleft()
    for i in g[v]:
        if d[i] is None:
            d[i] = d[v] + 1
            ans[i] = v
            queue.append(i)


print("Yes")
for i in range(2, len(ans)):
    print(ans[i])
