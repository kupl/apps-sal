def dfs(a, b, v, e):
    if a == b:
        return True
    v[a] = True
    for x in e[a]:
        if not v[x] and dfs(x, b, v, e):
            return True
    return False


a, e = [], []
for i in range(int(input())):
    t, x, y = map(int, input().split())
    if t == 1:
        a.append((x, y))
        e.append([])
        for i, ai in enumerate(a):
            if x in range(ai[0] + 1, ai[1]) or y in range(ai[0] + 1, ai[1]):
                e[-1].append(i)
            if ai[0] in range(x + 1, y) or ai[1] in range(x + 1, y):
                e[i].append(len(a) - 1)
    else:
        print('YES' if dfs(x - 1, y - 1, [False] * len(a), e) else 'NO')
