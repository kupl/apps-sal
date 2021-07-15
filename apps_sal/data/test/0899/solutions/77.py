n, m = map(int, input().split())
INF = 10**10
d = [[INF]*n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    d[a-1][b-1] = c
    d[b-1][a-1] = c
nxt = [[[i] for i in range(n)] for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if d[i][k]+d[k][j] < d[i][j]:
                d[i][j] = d[i][k]+d[k][j]
                nxt[i][j] = nxt[i][k][:]
            elif d[i][k]+d[k][j] == d[i][j]:
                nxt[i][j] += nxt[i][k]
s = set()
for start in range(n):
    for goal in range(n):
        if start==goal:
            continue
        def DFS(i):
            for j in nxt[i][goal]:
                s.add((i, j))
                if j!=goal:
                    DFS(j)
        DFS(start)
print(m-len(s)//2)
