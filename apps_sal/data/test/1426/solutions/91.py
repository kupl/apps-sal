from collections import deque
inf = 10**12
n, m = map(int, input().split())
node = [[]for _ in range(n)]
dis = [inf] * (n * 3)
for _ in range(m):
    a, b = map(int, input().split())
    node[a - 1].append(b - 1)
s, t = map(int, input().split())
dis[(s - 1) * 3] = 0
queue = deque([(s - 1) * 3])
while queue:
    r = queue.popleft()
    p = (r % 3 + 1) % 3
    for x in node[r // 3]:
        if dis[x * 3 + p] == inf:
            dis[x * 3 + p] = dis[r] + 1
            queue.append(x * 3 + p)
print(dis[(t - 1) * 3] // 3 if dis[(t - 1) * 3] != inf else -1)
