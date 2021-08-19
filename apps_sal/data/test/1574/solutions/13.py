(n, m) = list(map(int, input().split()))
e = [set() for i in range(n + 1)]
E = []
for i in range(m):
    (a, b) = list(map(int, input().split()))
    E.append((a, b))
    e[a] |= {b}
    e[b] |= {a}
l = [0] * (n + 1)
for i in range(n + 1):
    l[i] = len(e[i])
lmin = 12000
for (a, b) in E:
    t = e[a] & e[b]
    for x in t:
        if a in e[x] and b in e[x]:
            w = l[a] + l[b] + l[x] - 6
            if lmin > w:
                lmin = w
print(-1 if lmin == 12000 else lmin)
