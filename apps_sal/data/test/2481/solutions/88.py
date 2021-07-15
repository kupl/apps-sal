h, w = list(map(int, input().split()))

g = []
for _ in range(10):
    a = list(map(int, input().split()))
    g.append(a)

for k in range(10):
    for i in range(10):
        for j in range(10):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])

ans = 0
for i in range(h):
    ans += sum([g[x][1] for x in [x for x in map(int, input().split()) if x != -1]])
print(ans)

