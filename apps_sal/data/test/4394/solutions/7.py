a = input().split()
n, m = int(a[0]), int(a[1])
f = [i for i in range(0, n + 1)]


class edge:
    def __init__(self, U, V, W):
        self.u = U
        self.v = V
        self.w = W


l = []
for i in range(m):
    a = input().split()
    u, v, w = int(a[0]), int(a[1]), int(a[2])
    l.append(edge(u, v, w))
l.sort(key=lambda x: x.w)


def r(a):
    if a != f[a]:
        f[a] = r(f[a])
    return f[a]


cnt = 0
i = 0
while i < m:
    j = i
    while l[i].w == l[j].w:
        j = j + 1
        if j == m:
            break
    num = 0
    for k in range(i, j):
        x = r(l[k].u)
        y = r(l[k].v)
        if x != y:
            num = num + 1
    for k in range(i, j):
        x = r(l[k].u)
        y = r(l[k].v)
        if x != y:
            f[y] = x
            num = num - 1
    cnt = cnt + num
    i = j
print(cnt)
