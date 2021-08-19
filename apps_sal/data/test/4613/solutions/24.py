(n, m) = map(int, input().split())
list_AB = [list(map(int, input().split(' '))) for _ in range(m)]
ans = 0
for i in range(m):
    route = [[] for _ in range(n)]
    for j in range(m):
        if j != i:
            (a, b) = (list_AB[j][0], list_AB[j][1])
            route[a - 1].append(b - 1)
            route[b - 1].append(a - 1)
    q = [0]
    l = {0}
    while q:
        x = q.pop(0)
        for p in route[x]:
            if p not in l:
                l.add(p)
                q.append(p)
    if len(list(l)) != n:
        ans += 1
print(ans)
