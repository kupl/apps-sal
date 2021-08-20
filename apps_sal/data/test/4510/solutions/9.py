from collections import deque
(n, k) = list(map(int, input().split()))
q = deque()
a = list(map(int, input().split()))
vis = set()
for i in range(n):
    if len(q) < k:
        if a[i] not in vis:
            q.append(a[i])
            vis.add(a[i])
    elif a[i] not in vis:
        q.append(a[i])
        vis.remove(q.popleft())
        vis.add(a[i])
print(len(q))
print(str(list(q)[::-1]).replace('[', '').replace(']', '').replace(', ', ' '))
