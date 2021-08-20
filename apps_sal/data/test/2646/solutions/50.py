from collections import deque
(n, m) = list(map(int, input().split()))
print('Yes')
g = [[] for i in range(n)]
for i in range(m):
    (a, b) = list(map(int, input().split()))
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
q = deque([])
q.append(0)
check = [0] * n
while len(q) > 0:
    e = q.popleft()
    for i in g[e]:
        if check[i] > 0:
            continue
        check[i] = e + 1
        q.append(i)
for i in range(1, n):
    print(check[i])
