from collections import defaultdict


def f(u, v):
    s, l = [], len(v)
    i = j = 0
    for i in range(len(u)):
        while v[j][1] <= u[i][0]:
            j += 1
            if j == l:
                return s
        if u[i][1] <= v[j][0]:
            continue
        if u[i][0] >= v[j][0]:
            s.append(u[i])
        else:
            s.append((v[j][0], u[i][1]))
    return s


n, m = map(int, input().split())
p = defaultdict(list)

for i in range(m):
    x, y = map(int, input().split())
    p[x].append(y)

for x in p:
    if len(p[x]) > 1:
        p[x].sort()
    t, i = [], 1
    for j in p[x]:
        if i != j:
            t.append((i, j))
        i = j + 1
    if i != n + 1:
        t.append((i, n + 1))
    p[x] = t

k, s = 1, [(1, 2)]
for x in sorted(p.keys()):
    if x == k:
        s = f(p[x], s)
    else:
        s = f(p[x], [(s[0][0], n + 1)])
    if not s:
        break
    k = x + 1

if s and k == n + 1 and s[-1][1] != k:
    s = []
print(2 * (n - 1) if s else -1)
