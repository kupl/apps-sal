from collections import deque
(n, m) = list(map(int, input().split()))
uv = [list(map(int, input().split())) for _ in range(m)]
(s, t) = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for v in uv:
    graph[v[0] - 1].append(v[1] - 1)
s -= 1
t -= 1
is_checked = [[0] * 3 for _ in range(n)]
is_checked[s][0] = 1
ans = -1
q = deque()
q.append([s, 0])
while q:
    (v, cnt) = q.popleft()
    if v == t and cnt % 3 == 0:
        ans = cnt // 3
        break
    for i in graph[v]:
        if is_checked[i][(cnt + 1) % 3] == 0:
            q.append([i, cnt + 1])
            is_checked[i][(cnt + 1) % 3] = 1
print(ans)
