n, d, k = list(map(int, input().split()))

if d+1 > n:
    print('NO')
    return

ans = []
dist = [0]*n
deg = [0]*n
for i in range(d+1):
    if i == 0 or i == d:
        deg[i] = 1
    else:
        deg[i] = 2
    if i != d:
        ans.append((i+1, i+2))
    dist[i] = max(i, d-i)

for i in range(n):
    if deg[i] > k:
        print('NO')
        return

from collections import deque
q = deque(list(range(d+1)))
cur = d+1
while q and cur < n:
    v = q.popleft()
    if dist[v] < d and deg[v] < k:
        deg[v] += 1
        dist[cur] = dist[v]+1
        deg[cur] = 1
        ans.append((v+1, cur+1))
        q.append(v)
        q.append(cur)
        cur += 1
    else:
        continue
if cur != n:
    print('NO')
else:
    print('YES')
    for i in range(len(ans)):
        print(*ans[i])

