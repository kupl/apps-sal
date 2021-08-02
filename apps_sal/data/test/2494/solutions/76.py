from collections import deque
K = int(input())

d = [1000000 for x in range(K + 1)]
d[1] = 0


def bfs(K):
    q = deque()
    q.append(1)
    while q:
        nx = q.popleft()
        if d[(nx * 10) % K] > d[nx]:
            d[(nx * 10) % K] = d[nx]
            q.appendleft((nx * 10) % K)
        if d[(nx + 1) % K] > d[nx] + 1:
            d[(nx + 1) % K] = d[nx] + 1
            q.append((nx + 1) % K)
    return d[0] + 1


print(bfs(K))
