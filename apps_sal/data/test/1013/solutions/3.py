n, m = list(map(int, input().split()))
a = []
g = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            g.append((i, j))
l = len(g)
two = False
for i in range(l):
    if g[i][0] == 0 or g[i][1] == 0 or g[i][0] == (n - 1) or g[i][1] == (m - 1):
        two = True
        break
if two:
    print(2)
else:
    print(4)
