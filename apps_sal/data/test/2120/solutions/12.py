n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(enumerate(u, 1))
v.sort(key=lambda x: x[1], reverse=True)
s, u = 0, [0] + u
p = [[] for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    p[x].append(y)
    p[y].append(x)
for x, f in v:
    for y in p[x]: s += u[y]
    u[x] = 0
print(s)
