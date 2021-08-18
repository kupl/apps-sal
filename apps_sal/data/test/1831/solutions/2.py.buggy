l = []
were = []


def dfs(v):
    nonlocal l, were
    if not were:
        were = len(l) * [False]
    were[v] = True
    for i in l[v]:
        if not were[i]:
            dfs(i)


n, m = list(map(int, input().split()))
if m != n - 1:
    print("no")
else:
    l = [[] for i in range(n)]
    for i in range(m):
        a, b = list(map(int, input().split()))
        l[a - 1].append(b - 1)
        l[b - 1].append(a - 1)

    dfs(0)
    f = True
    for i in were:
        f = f and i

    if f:
        print("yes")
    else:
        print("no")
