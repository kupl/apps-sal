def read_data():
    n, m = map(int, input().split())
    Es = [[] for i in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        Es[u].append(v)
        Es[v].append(u)
    return n, m, Es

def solve(n, m, Es):
    if n - 1 not in Es[0]:
        return shortestpath(n, Es)
    else:
        Es = trans(n, Es)
        return shortestpath(n, Es)

def trans(n, Es):
    Emat = [[False] * n for i in range(n)]
    for i, row in enumerate(Es):
        for j in row:
            Emat[i][j] = True
    nEs = [[] for i in range(n)]
    for u in range(n):
        for v in range(n):
            if u == v:
                continue
            if Emat[u][v]:
                continue
            nEs[u].append(v)
    return nEs

def shortestpath(n, Es):
    visited = [False] * n
    visited[0] = True
    steps = 0
    fs = [0]
    while fs:
        nfs = []
        for f in fs:
            if f == n - 1:
                return steps
            for v in Es[f]:
                if visited[v]:
                    continue
                nfs.append(v)
                visited[v] = True
        fs = nfs
        steps += 1
    return -1

n, m, Es = read_data()
print(solve(n, m, Es))
