from collections import deque
N = int(input())
visited = [-1] * N
l = [[] for i in range(N)]
for i in range(N - 1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    l[a].append((b, c % 2))
    l[b].append((a, c % 2))


def ans(node, dis):
    visited[node] = 0
    que = deque(l[node])
    while que:
        node, dis = que.popleft()
        visited[node] = dis
        for i, j in l[node]:
            if visited[i] == -1:
                visited[i] = (dis + j) % 2
                que.append((i, (dis + j) % 2))


ans(0, 0)
for i in visited:
    print(i)
