n = int(input())
g = {i: set() for i in range(1, n + 1)}
d = {i: set() for i in range(1, n + 1)}
for i in range(1, n + 1):
    (x, y) = list(map(int, input().split()))
    g[x].add(y)
    g[y].add(x)
    d[i].add(x)
    d[i].add(y)
a = [1]
b = set(a)
i = 1
c = 0
while c < n:
    x = g[i]
    y = d[i]
    for j in y:
        if j in x and j not in b:
            a.append(j)
            b.add(j)
            i = j
            break
    c += 1
print(*a)
