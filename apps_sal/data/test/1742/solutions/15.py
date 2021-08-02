n, m = [int(x) for x in input().split()]

p = [int(x) - 1 for x in input().split()]

e = [[] for _ in range(n)]

for _ in range(m):
    u, v = [int(x) for x in input().split()]
    e[u - 1].append(v - 1)

t = [p[n - 1]]

ans = 0
for i in range(n - 2, -1, -1):
    u = p[i]
    if len(e[u]) >= len(t):
        f = set(e[u])
        can = True
        for x in t:
            if x not in f:
                can = False
                break
        if can:
            ans += 1
        else:
            t.append(u)
    else:
        t.append(u)


print(ans)
