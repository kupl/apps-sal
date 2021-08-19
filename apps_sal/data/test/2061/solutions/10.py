(x, y, k) = list(map(int, input().split()))
a = [input().strip() for i in range(x)]
m = [[0 if j == '*' else 1 for j in i] for i in a]
m1 = [[0 if j == '*' else 1 for j in i] for i in a]
lk = []


def bfs(m, i, j):
    q = set()
    s = 0
    f = 1
    q.add((i, j))
    while q:
        (ax, ay) = q.pop()
        m[ax][ay] = 0
        s += 1
        if ax == 0 or ay == 0 or ax == x - 1 or (ay == y - 1):
            f = 0
        if ax < x - 1 and m[ax + 1][ay]:
            q.add((ax + 1, ay))
        if ax > 0 and m[ax - 1][ay]:
            q.add((ax - 1, ay))
        if ay < y - 1 and m[ax][ay + 1]:
            q.add((ax, ay + 1))
        if ay > 0 and m[ax][ay - 1]:
            q.add((ax, ay - 1))
    return (f, s)


for i in range(x):
    for j in range(y):
        if m1[i][j]:
            (f, s) = bfs(m1, i, j)
            if f:
                lk.append((s, i, j))
lk.sort()
k1 = len(lk)
sal = 0
for e in range(k1 - k):
    (s, i, j) = lk[e]
    sal += s
    bfs(m, i, j)
print(sal)
for i in range(x):
    print(''.join(['.' if j else '*' for j in m[i]]))
