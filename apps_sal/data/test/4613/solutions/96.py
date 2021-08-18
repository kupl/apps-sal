n, m = map(int, input().split())
par = [i for i in range(n + 1)]


def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def same(x, y):
    return find(x) == find(y)


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    par[x] = y


ls = [list(map(int, input().split())) for _ in range(m)]
ans = 0
for i in ls:
    for k in ls:
        if i != k:
            [a, b] = k
            unite(a, b)
    flag = True
    for p in range(1, n + 1):
        for q in range(1, n + 1):
            if not same(p, q):
                flag = False
                break
        if flag == False:
            break
    if flag == False:
        ans += 1
    par = [i for i in range(n + 1)]
print(ans)
