from collections import deque
n = int(input())
ans = [-1] * n
ans[0] = 0
d = [[] for _ in range(n)]

for i in range(n - 1):
    u, v, w = map(int, input().split())
    d[u - 1].append([v - 1, w])
    d[v - 1].append([u - 1, w])

cnt = 0
queue = deque()
queue.append(0)
while queue:
    u = queue.pop()
    for v, w in d[u]:
        if ans[v] == -1:
            if w % 2 == 0:
                ans[v] = ans[u]
            else:
                ans[v] = ans[u] ^ 1
            queue.append(v)


for i in range(n):
    print(ans[i])
