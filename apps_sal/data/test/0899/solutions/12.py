def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


n, w = map(int, input().split(" "))

a = []

d = [[10 ** 10] * n for i in range(n)]
k = [n for i in range(n)]

for i in range(w):
    x, y, z = map(int, input().split(" "))
    d[x - 1][y - 1] = z
    d[y - 1][x - 1] = z
    a.append([x, y, z])
for i in range(n):
    d[i][i] = 0

d = warshall_floyd(d)

ans = w
for i in range(len(a)):
    for s in range(n):
        if d[s][a[i][1] - 1] + a[i][2] == d[s][a[i][0] - 1]:
            ans -= 1
            break

print(ans)
