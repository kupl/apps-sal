def dfs(v):
    pos.append(v)
    used[v] = 1
    for i in range(n):
        if s[v][i] == '1' and (not used[i]):
            dfs(i)


n = int(input())
a = list(map(int, input().split()))
s = [input() for _ in range(n)]
used = [0] * n
for i in range(n):
    if not used[i]:
        pos = []
        dfs(i)
        values = [a[i] for i in pos]
        pos.sort()
        values.sort()
        for (i, j) in enumerate(pos):
            a[j] = values[i]
print(' '.join((str(x) for x in a)))
