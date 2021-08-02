
a = input().split()
n = int(a[0])
m = int(a[1])
g = []
for i in range(n):
    g.append(input().split())

mine = 4
for i in range(1, n - 1):
    if g[i][0] == '1' or g[i][m - 1] == '1':
        mine = 2
for i in range(1, m - 1):
    if g[0][i] == '1' or g[n - 1][i] == '1':
        mine = 2

print(mine)
