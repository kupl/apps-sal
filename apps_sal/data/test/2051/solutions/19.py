n, m, k = map(int, input().split())
a = list(map(int, input().split()))
tr = [[] for i in range(n)]

for i in range(m):
    l, r = map(int, input().split())
    tr[l - 1].append(r - 1)
    tr[r - 1].append(l - 1)
visited = [False for i in range(n)]
ans = 0
for i in range(n):
    if visited[i]: continue
    s = [i]
    visited[i] = True
    qeue = {}
    while s:
        x = s.pop()
        if a[x] not in qeue: qeue[a[x]] = 0
        qeue[a[x]] += 1
        for j in tr[x]:
            if visited[j]: continue
            visited[j] = True
            s.append(j)
    neu, maxi = 0, 0
    for e in qeue:
        maxi = max(maxi, qeue[e])
        neu += qeue[e]
    ans += neu - maxi
print(ans)
