import sys
input = sys.stdin.readline


def I():
    return list(map(int, input().split()))


(n, m) = I()
ed = [I() for i in range(m)]
ed.sort(key=lambda x: x[2])
p = [i for i in range(n)]


def find(x):
    while x != p[x]:
        x = p[x]
    return x


def union(a, b):
    x = find(a)
    y = find(b)
    if x != y:
        p[y] = p[x] = min(x, y)
        return 1
    return 0


an = 0
ce = 0
pos = [1] * m
i = 0
while ce < n - 1:
    (x, y, w) = ed[i]
    for j in range(i, m):
        if ed[j][2] != w:
            break
        (a, b, c) = ed[j]
        if find(a - 1) == find(b - 1):
            pos[j] = 0
    for j in range(i, m):
        (x, y, b) = ed[j]
        if ed[j][2] != w:
            break
        if pos[j]:
            d = union(x - 1, y - 1)
            if d == 0:
                an += 1
            else:
                ce += 1
    if ce == n - 1:
        break
    i = j
print(an)
