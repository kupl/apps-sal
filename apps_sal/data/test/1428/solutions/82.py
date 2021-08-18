n, c = list(map(int, input().split()))
d = [list(map(int, input().split())) for i in range(c)]
c_ = [list(map(int, input().split())) for i in range(n)]
g = [[] for i in range(3)]
for i in range(n):
    for j in range(n):
        g[(i + j + 2) % 3].append(c_[i][j] - 1)
'''
for i in range(c):
    for j in range(c):
        for k in range(c):
            d[i][j]=min(d[i][j],d[i][k]+d[k][j])
print(d)
'''
f = [[] for i in range(3)]
for i in range(3):
    for j in range(c):
        x = 0
        for k in g[i]:
            x += d[k][j]
        f[i].append((j, x))
    f[i] = sorted(f[i], key=lambda x: x[1])[:3]
ans = []
for i in f[0]:
    for j in f[1]:
        for k in f[2]:
            if i[0] != j[0] and k[0] != j[0] and i[0] != k[0]:
                ans.append(i[1] + j[1] + k[1])
print((min(ans)))
