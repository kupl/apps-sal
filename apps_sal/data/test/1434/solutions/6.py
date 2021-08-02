n = int(input())
f = [list(map(int, input().split())) for i in range(n)]
deg1 = []
edges = []
for i in range(n):
    if f[i][0] == 1:
        deg1.append(i)
while len(deg1):
    i = deg1.pop()
    if f[i][0] == 0:
        continue
    edges.append([i, f[i][1]])
    f[i][0] -= 1
    f[f[i][1]][0] -= 1
    f[f[i][1]][1] ^= i
    if f[f[i][1]][0] == 1:
        deg1.append(f[i][1])
print(len(edges))
for e in edges:
    print(e[0], e[1])
