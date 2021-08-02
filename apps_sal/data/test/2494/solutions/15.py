from collections import deque
k = int(input())
dist = [float('inf') for _ in range(k)]
dist[1] = 1
q = deque()
q.append(1)
while len(q) > 0:
    r = q.popleft()
    s = (r + 1) % k
    if dist[r] + 1 < dist[s]:
        dist[s] = dist[r] + 1
        q.append(s)
    t = (r * 10) % k
    if dist[r] < dist[t]:
        dist[t] = dist[r]
        q.appendleft(t)
print(dist[0])
