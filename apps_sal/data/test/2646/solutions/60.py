from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
ans = [-1] * (n - 1)
used = [0] * n
used[0] = 1
que = deque([0])
while que:
    posi = que.popleft()
    for p in graph[posi]:
        if not used[p]:
            que.append(p)
            ans[p - 1] = posi + 1
            used[p] = 1
print('Yes')
print(*ans, sep='\n')
