from collections import deque
(n, m) = map(int, input().split())
print('Yes')
root = [[] for _ in range(n)]
for i in range(m):
    (a, b) = map(int, input().split())
    root[a - 1].append(b - 1)
    root[b - 1].append(a - 1)
q = deque([0])
check = [0] * n
while q:
    e = q.popleft()
    for i in root[e]:
        if check[i]:
            continue
        check[i] = e + 1
        q.append(i)
for i in range(1, n):
    print(check[i])
