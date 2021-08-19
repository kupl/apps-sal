(n, m) = map(int, input().split())
a = list(map(int, input().split()))
(k, c, free) = (n // m, [[] for _ in range(m)], [])
for (i, ai) in enumerate(a):
    c[ai % m].append(i)
ans = 0
for _ in range(2 * m):
    i = _ % m
    lci = len(c[i])
    for j in range(k, lci)[::-1]:
        free.append((c[i][j], i))
        c[i].pop()
    for j in range(k - lci):
        if free:
            to_add = (i - free[-1][1]) % m
            ans += to_add
            a[free[-1][0]] += to_add
            c[i].append(free[-1][0])
            free.pop()
print(ans)
print(*a)
