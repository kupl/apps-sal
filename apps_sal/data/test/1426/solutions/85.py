from collections import deque
(n, m) = map(int, input().split())
adj_list = [[] for _ in range(3 * n)]
for _ in range(m):
    (u, v) = map(int, input().split())
    adj_list[3 * u - 3].append(3 * v - 2)
    adj_list[3 * u - 2].append(3 * v - 1)
    adj_list[3 * u - 1].append(3 * v - 3)
(s, t) = map(int, input().split())
dist = [-1] * (3 * n)
queue = deque([3 * s - 3])
dist[3 * s - 3] = 0
while queue:
    vertex = queue.popleft()
    for next_vertex in adj_list[vertex]:
        if dist[next_vertex] != -1:
            continue
        dist[next_vertex] = dist[vertex] + 1
        queue.append(next_vertex)
t_distance = dist[3 * t - 3]
if t_distance == -1:
    print(-1)
else:
    print(t_distance // 3)
