n, m = map(int, input().split())
e = [set() for i in range(n + 1)]
E = []
mi = 1000000000000
for i in range(m):
    a, b = map(int, input().split())
    E += [(a, b)]
    e[a] |= {b}
    e[b] |= {a}
l = [len(e[i]) for i in range(n + 1)]
for a, b in E:
    t = e[a] & e[b]
    for x in t:
        if a in e[x] and b in e[x]:
            k = l[a] + l[b] + l[x] - 6
            if k < mi:
                mi = k
print(-1 if mi == 1000000000000 else mi)
