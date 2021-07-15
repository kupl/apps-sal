n = int(input())
g = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = [int(x) for x in input().split()]
    g[a].append(b)
    g[b].append(a)

d = [0 for i in range(n+1)]
v = [0 for i in range(n+1)]
e = [0 for i in range(n+1)]
p = [0.0 for i in range(n+1)]
p[1] = 1.0
en = 0
q = [1]
while len(q):
    c = q.pop(0)
    v[c] = 1
    a = 0
    for ne in g[c]:
        if not v[ne]:
            q.append(ne)
            d[ne] = d[c] + 1
            p[ne] = p[c]/len(g[c]) if c == 1 else p[c]/(len(g[c])-1)
            a += 1
    if a == 0:
        e[c] = 1
        en += 1
ave = 0.0
for i in range(n+1):
    if e[i]:
        ave += d[i]*p[i]
print(ave)

