n = int(input())
p = list(map(int, input().split()))
vis = [False] * n
nv = 0
m = 0
cyc = []
while nv < n:
    while vis[m]:
        m += 1
    temp = []
    c = m
    while not vis[c]:
        temp.append(c)
        nv += 1
        vis[c] = True
        c = p[c] - 1
    cyc.append(temp)
size = []
for i in range(len(cyc)):
    size.append(len(cyc[i]))
size = sorted(size)
if len(size) == 1:
    print(size[0] * size[0])
else:
    out = (size[len(size) - 1] + size[len(size) - 2]) * (size[len(size) - 1] + size[len(size) - 2])
    for i in range(len(size) - 2):
        out += size[i] * size[i]
    print(out)
