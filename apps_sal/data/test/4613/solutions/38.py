N, M = list(map(int, input().split()))
AB = [tuple(map(int, input().split())) for _ in range(M)]


def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    par[x] = y


cnt = 0
for i in range(M):
    par = [i for i in range(N + 1)]
    k = 0
    for a, b in AB:
        if k != i:
            unite(a, b)
        k += 1

    res = []
    for j in range(1, N + 1):
        res.append(find(j))

    if len(set(res)) >= 2:
        cnt += 1
print(cnt)
