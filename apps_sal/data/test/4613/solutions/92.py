(N, M) = list(map(int, input().split()))
a = []
b = []
for e in range(M):
    (x, y) = list(map(int, input().split()))
    x -= 1
    y -= 1
    a.append(x)
    b.append(y)


def solve(e):
    parent = [i for i in range(N)]

    def find(x, parent):
        y = parent[x]
        while y != parent[y]:
            y = find(y, parent)
        parent[x] = y
        return y

    def unite(a, b, parent):
        x = find(a, parent)
        y = find(b, parent)
        if x != y:
            parent[x] = y
    for i in range(M):
        if i == e:
            continue
        unite(a[i], b[i], parent)
    cnt = [0 for _ in range(N)]
    for i in range(N):
        cnt[find(i, parent)] = 1
    if cnt.count(1) > 1:
        return 1
    else:
        return 0


ans = 0
for i in range(M):
    ans += solve(i)
print(ans)
