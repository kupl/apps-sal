from collections import deque
n, m = map(int, input().split())
edge = [[] for i in range(n)]
kkp = [0] * n
for i in range(m):
    u, v = map(int, input().split())
    edge[u - 1].append(v - 1)
s, t = map(int, input().split())
que = deque([(s - 1, 0)])
while que:
    now, dis = que.popleft()
    for next in edge[now]:
        if next == t - 1 and (dis + 1) % 3 == 0:
            print((dis + 1) // 3)
            return
        if not kkp[next] & (2 ** ((dis + 1) % 3)):
            kkp[next] = kkp[next] | (2 ** ((dis + 1) % 3))
            que.append((next, dis + 1))
print(-1)
