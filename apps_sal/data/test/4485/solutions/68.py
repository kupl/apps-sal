from collections import deque
n, m = map(int, input().split())
E = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    E[a-1].append(b-1)
    E[b-1].append(a-1)
dis = [200000 for i in range(n)]
dis[0] = 0
Q = deque([0])
while Q:
    now = deque.popleft(Q)
    for i in E[now]:
        if dis[i] == 200000:
            dis[i] = dis[now]+1
            deque.append(Q, i)
print("POSSIBLE" if dis[-1] == 2 else "IMPOSSIBLE")
