n, m = map(int, input().split())
cats = list(map(int, input().split()))
graf = [[] for i in range(n)]
ans = 0
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graf[a].append(b)
    graf[b].append(a)
q = [(0, 0, 0)]
while len(q) != 0:
    v, catind, prev = q.pop()
    if cats[v]:
        catind += 1
    else:
        catind = 0
    if catind > m:
        continue
    if len(graf[v]) == 1 and v:
        ans += 1
        continue
    for i in graf[v]:
        if i == prev:
            continue
        q.append((i, catind, v))
print(ans)
