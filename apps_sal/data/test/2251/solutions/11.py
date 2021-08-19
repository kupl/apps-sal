def dfs(u1, v1, c):
    ret = False
    used[u1 - 1] = True
    for (i, edge) in enumerate(e):
        if edge[2] != c:
            continue
        t = None
        if u1 == edge[0]:
            t = edge[1]
        elif u1 == edge[1]:
            t = edge[0]
        if t and (not used[t - 1]):
            if t == v1:
                return True
            else:
                ret |= dfs(t, v1, c)
    return ret


(n, m) = map(int, input().split())
e = [list(map(int, input().split())) for i in range(m)]
used = [False for i in range(n)]
q = int(input())
a = []
for i in range(q):
    (u, v) = map(int, input().split())
    ans = 0
    for c in range(1, m + 1):
        if dfs(u, v, c):
            ans += 1
        used = [False for i in range(n)]
    a += [ans]
for i in a:
    print(i)
