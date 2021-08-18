

from collections import deque

n, m = list(map(int, input().split()))
g = [set([]) for _ in range(n)]
for i in range(m):
    a, b = list(map(int, input().split()))
    a, b = a - 1, b - 1
    g[a].add(b)

s, t = list(map(int, input().split()))
s, t = s - 1, t - 1

q = deque()
level = [[-1] * n for i in range(3)]
q.append((s, 0))
level[0][s] = 0
while len(q) > 0:
    cur, hp = q.popleft()
    lvl = level[hp][cur]
    for i in g[cur]:
        if level[(hp + 1) % 3][i] == -1:
            level[(hp + 1) % 3][i] = lvl + 1
            q.append((i, (hp + 1) % 3))
print((level[0][t] // 3))
