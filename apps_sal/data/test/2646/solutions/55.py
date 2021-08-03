from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

ans = [-1] * (n - 1)

q = deque()
q.append(0)
used = {0}
while q:
    node = q.popleft()
    for next_node in graph[node]:
        if next_node in used:
            continue
        q.append(next_node)
        used.add(next_node)
        ans[next_node - 1] = node + 1

print('Yes')
print(*ans, sep='\n')
