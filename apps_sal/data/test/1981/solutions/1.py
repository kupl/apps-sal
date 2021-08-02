from collections import deque
n, m = tuple(map(int, input().split()))
is_cat = tuple(map(int, input().split()))

p = [[] for i in range(n)]
for i in range(n - 1):
    x, y = list(map(int, input().split()))
    p[x - 1].append(y - 1)
    p[y - 1].append(x - 1)


q = deque([(0, is_cat[0])])
used = [0] * n
res = 0
while len(q) > 0:
    u, c = q.popleft()
    used[u] = 1
    ok = False
    for v in p[u]:
        if used[v]:
            continue
        ok = True
        if is_cat[v] and is_cat[v] + c <= m:
            q.append((v, c + is_cat[v]))
        elif not is_cat[v]:
            q.append((v, 0))
    if not ok:
        res += 1


print(res)
