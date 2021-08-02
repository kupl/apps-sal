n, m = map(int, input().split())
r = list(enumerate(map(int, input().split()), 1))
r.sort(key=lambda x: x[1])
s, p = 0, [[] for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    p[x].append(y)
    p[y].append(x)
q = [len(t) for t in p]
for x, f in r:
    s += f * q[x]
    for y in p[x]: q[y] -= 1
print(s)
