from collections import deque

K = int(input())

visited = [False] * K
Q = deque([(1, 1)])

while True:
    s, v = Q.popleft()
    if v == 0:
        print(s)
        return

    if visited[v]:
        continue
    visited[v] = True

    Q.appendleft((s, (10 * v) % K))
    Q.append((s + 1, (v + 1) % K))
