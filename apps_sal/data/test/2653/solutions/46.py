import collections

n, q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n - 1)]
px = [list(map(int, input().split())) for _ in range(q)]

c = [[] for _ in range(n)]
for a, b in ab:
    a, b = a - 1, b - 1
    c[a].append(b)
    c[b].append(a)

point = [0] * n
for p, x in px:
    point[p - 1] += x

parents = [0] * n
ans = [0] * n
q = collections.deque()
q.append(0)
while q:
    v = q.pop()
    ans[v] = ans[parents[v]] + point[v]
    for i in c[v]:
        if i == parents[v]:
            continue
        parents[i] = v
        q.append(i)
print(' '.join(list(map(str, ans))))
