n = int(input())
x = []
y = []
for i in range(n):
    xx, yy = map(int, input().split())
    x.append([xx, i])
    y.append([yy, i])
x.sort()
y.sort()
px = []
py = []
for i in range(n - 1):
    px.append([x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]])
    py.append([y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]])
p = px + py
x = []
y = []
px = []
py = []
p.sort()
r = [i for i in range(n)]
rank = [1 for i in range(n)]


def root(x):
    if x == r[x]:
        return x
    else:
        r[x] = root(r[x])
        return r[x]


def union(path):
    rx = root(path[1])
    ry = root(path[2])
    if rx == ry:
        return 0
    else:
        if rank[rx] > rank[ry]:
            r[rx] = ry
            rank[rx] += rank[ry]
        else:
            r[ry] = rx
            rank[ry] += rank[rx]
        return path[0]


ans = 0
for i in range(len(p)):
    ans += union(p[i])
print(ans)
