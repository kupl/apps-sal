from collections import deque

n, m = map(int, input().split())
c = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    c[a].append(b)
    c[b].append(a)

if len(c[0]) == 0:
    print('No')
    return

l = [0] * n
l[0] = 1
q = deque()
for i in c[0]:
    q.append(i)
    l[i] = 1
while q:
    p = q.pop()
    for i in c[p]:
        if l[i] == 0:
            l[i] = p + 1
            q.appendleft(i)

print('Yes')
for i in range(1, n):
    print(l[i])
