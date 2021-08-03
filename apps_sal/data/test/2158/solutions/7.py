def dfs(d, di):
    stack = [[0, 0]]
    mark = {i: False for i in range(n)}
    mark[0] = True
    res = []
    while stack:
        s = stack.pop()
        x, cost = s[0], s[1]
        res.append(cost)
        for i, y in enumerate(d[x]):
            if mark[y] == False:
                if di.get((x, y)) == None:
                    new_cost = di[(y, x)]
                else:
                    new_cost = di[(x, y)]
                stack.append([y, cost + new_cost])
                mark[y] = True
    print(max(res))


n = int(input())
di, d = {}, {}
for i in range(n - 1):
    u, v, c = map(int, input().split())
    di[(u, v)] = c
    if d.get(u) == None:
        d[u] = []
    if d.get(v) == None:
        d[v] = []
    d[u].append(v)
    d[v].append(u)
dfs(d, di)
