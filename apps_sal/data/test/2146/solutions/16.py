n = int(input())
a = list(map(int, input().split()))

g = []

for i in range(n):
    To = set()
    if i < n - 1:
        To.add(i+1)
    if i > 0:
        To.add(i-1)
    if a[i] - 1 != i:
        To.add(a[i]-1)
    g.append(To)

q = [0]
used = [i == 0 for i in range(n)]
d = [0 for i in range(n)]
p = [0 for i in range(n)]
p[0] = -1

while len(q) > 0:
    v = q[0]
    q.pop(0)

    for to in g[v]:
        if not used[to]:
            used[to] = True
            q.append(to)
            d[to] = d[v] + 1
            p[to] = v

for r in d:
    print(r, end=' ')

