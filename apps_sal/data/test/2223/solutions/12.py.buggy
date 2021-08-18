n = int(input())
if n & 1 > 0:
    print(-1)
    return
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
c = [1] * n
v = [-1] * n
v[0] = 0
s = [0]
while s:
    x = s[-1]
    k = False
    for j in g[x]:
        if v[j] == -1:
            v[j] = x
            s.append(j)
            k = True
    if not k:
        s.pop()
        c[v[x]] += c[x]
o = 0
for j in c[1:]:
    if j & 1 < 1:
        o += 1
print(o)
