f = lambda: map(int, input().split())
g = lambda: [[] for x in range(n)]
n, k = f()
n += 1

s, p = [], list(f())
c, d = [0] * n, [0] * n
u, v = g(), g()

for x in range(1, n):
    t = list(f())
    m = t.pop(0)
    if m:
        c[x] = m
        v[x] = t
        for y in t: u[y].append(x)
    else:
        s.append(x)
        d[x] = 1
while s:
    x = s.pop()
    for y in u[x]:
        c[y] -= 1
        d[y] = max(d[y], d[x] + 1)
        if c[y] == 0: s.append(y)

if any(c[x] for x in p):
    print(-1)
    return

q = [0] * n
while p:
    x = p.pop()
    if q[x] == 0:
        p += v[x]
        q[x] = 1

p = sorted((d[x], x) for x in range(n) if q[x])
print(len(p))
for d, x in p: print(x)
