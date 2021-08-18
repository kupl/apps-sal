n = int(input())
c = []
d = []
for i in range(n):
    x, y = map(int, input().split())
    c.append((x, y))
opt = {}
for i in range(n):
    x, y = map(int, input().split())
    d.append((x, y))
    for ic in c:
        k = (x + ic[0], y + ic[1])
        if k not in opt:
            opt[k] = 0
        opt[k] += 1

for o in opt:
    if opt[o] >= n:
        print(o[0], o[1])
        return
