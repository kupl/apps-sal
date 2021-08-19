(n, k) = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
mod = 998244353
ans = 1
parent = [i + 1 for i in range(n)]
rank = [0 for i in range(n)]
size = [1 for i in range(n)]


def find(x):
    if parent[x - 1] == x:
        return x
    else:
        parent[x - 1] = find(parent[x - 1])
        return parent[x - 1]


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x - 1] < rank[y - 1]:
        parent[x - 1] = y
        size[y - 1] += size[x - 1]
    else:
        parent[y - 1] = x
        size[x - 1] += size[y - 1]
        if rank[x - 1] == rank[y - 1]:
            rank[x - 1] += 1


for i in range(n):
    for j in range(i + 1, n):
        flag = True
        for l in range(n):
            if a[l][i] + a[l][j] > k:
                flag = False
                break
        if flag == True:
            unite(i + 1, j + 1)
for i in range(n):
    if find(i + 1) == i + 1:
        for j in range(size[i]):
            ans *= j + 1
            ans %= mod
parent = [i + 1 for i in range(n)]
rank = [0 for i in range(n)]
size = [1 for i in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        flag = True
        for l in range(n):
            if a[i][l] + a[j][l] > k:
                flag = False
                break
        if flag == True:
            unite(i + 1, j + 1)
for i in range(n):
    if find(i + 1) == i + 1:
        for j in range(size[i]):
            ans *= j + 1
            ans %= mod
print(ans)
