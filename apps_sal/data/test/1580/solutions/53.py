n, m = map(int, input().split())

parent = [i + 1 for i in range(n)]
rank = [0 for i in range(n)]


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
    else:
        parent[y - 1] = x
        if rank[x - 1] == rank[y - 1]:
            rank[x - 1] += 1


for i in range(m):
    x, y, z = map(int, input().split())
    unite(x, y)
ans = n
for i in range(n):
    if find(i + 1) != i + 1:
        ans -= 1
print(ans)
