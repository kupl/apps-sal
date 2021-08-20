(n, m, c) = list(map(int, input().split()))
l = list(map(int, input().split()))
qa = n
d = [[] for i in range(n + 1)]
Visited = [False for i in range(n + 1)]
f = 0
L = []
for i in range(m):
    (a, b) = list(map(int, input().split()))
    d[a].append(b)
    d[b].append(a)
    L.append([a, b])
ma = 0
d1 = {}
for x in l:
    q = [x]
    r = 0
    t = 0
    while q:
        v = q[0]
        r += 1
        Visited[v] = True
        t += len(d[v])
        for y in d[v]:
            if Visited[y] == False:
                q.append(y)
                Visited[y] = True
        del q[0]
    qa -= r
    d1[r] = d1.get(r, []) + [t]
for x in L:
    if Visited[x[0]] == Visited[x[1]] == False:
        f += 1
rr = True
y = sorted(d1, reverse=True)
out = -f
for x in y:
    for e in d1[x]:
        if rr:
            u = qa + x
            out += u * (u - 1) // 2 - e // 2
            rr = False
        else:
            out += x * (x - 1) // 2 - e // 2
print(out)
