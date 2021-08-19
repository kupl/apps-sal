def dfs(v):
    pos.append(v)
    used[v] = True
    for g in range(n):
        if int(s[v][g]) and (not used[g]):
            dfs(g)


n = int(input())
p = list(map(int, input().split()))
s = [input() for i in range(n)]
used = [False] * n
for j in range(n):
    if not used[j]:
        pos = []
        dfs(j)
        values = [p[i] for i in pos]
        pos.sort()
        values.sort()
        for (i, po) in enumerate(pos):
            p[po] = values[i]
print(' '.join([str(x) for x in p]))
