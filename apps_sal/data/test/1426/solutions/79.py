from collections import deque
(n, m) = map(int, input().split())
l = [[] for i in range(n + 1)]
rl = [[-1 for i in range(n + 1)] for i in range(3)]
for i in range(m):
    (u, v) = map(int, input().split())
    l[u].append(v)
(s, t) = map(int, input().split())
d = deque()
ans = -1
d.append([s, 0])
rl[0][s] = 0
while len(d):
    (now, count) = d.popleft()
    for i in l[now]:
        if i == t and count % 3 == 2:
            ans = (count + 1) // 3
            break
        elif rl[(count % 3 + 1) % 3][i] == -1:
            d.append([i, count + 1])
            rl[(count % 3 + 1) % 3][i] = count + 1
    if ans >= 0:
        break
print(ans)
