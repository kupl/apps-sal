(n, m) = map(int, input().split())
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


def nc2(a):
    return a * (a - 1) // 2


ab = []
for i in range(m):
    ab.append(list(map(int, input().split())))
ab.reverse()
ans = [0]
for i in range(m):
    (a, b) = (ab[i][0], ab[i][1])
    num_a = size[find(a) - 1]
    num_b = size[find(b) - 1]
    unite(a, b)
    num = size[find(a) - 1]
    if num_a != num:
        ans.append(ans[-1] + nc2(num) - nc2(num_a) - nc2(num_b))
    else:
        ans.append(ans[-1])
ans.reverse()
num = nc2(n)
for i in range(m):
    print(num - ans[i + 1])
