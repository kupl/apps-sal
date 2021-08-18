n = int(input())
c = [list(map(int, input().split())) for _ in range(3)]
g = [[] for _ in range(n)]
l = [0] * n
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
    l[a - 1] += 1
    l[b - 1] += 1
if max(l) > 2:
    print(-1)
    return
for i in range(n):
    if l[i] == 1:
        s = [i]
        break
dist = [-1] * n
dist[i] = 0
while s:
    d = s.pop()
    dist[d] %= 3
    for node in g[d]:
        if dist[node] == -1:
            s.append(node)
            dist[node] = dist[d] + 1
ans = float('inf')
for i1 in range(3):
    for i2 in range(3):
        if i1 == i2:
            continue
        for i3 in range(3):
            if i1 == i3 or i2 == i3:
                continue
            tmp = 0
            for j in range(n):
                tmp += c[(i1, i2, i3)[dist[j]]][j]
            if tmp < ans:
                idx = (i1, i2, i3)
                ans = tmp
print(ans)
for i in range(n - 1):
    print(idx[dist[i]] + 1, end=' ')
print(idx[dist[n - 1]] + 1)
