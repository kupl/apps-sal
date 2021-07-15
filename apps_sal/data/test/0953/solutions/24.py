n = int(input())
t = list(map(int, input().split()))
a = [input() for i in range(n)]
u = [0] * n
def dfs(i):
    p.append(i)
    u[i] = 1
    for j in range(n):
        if a[i][j] == '1' and not u[j]:
            dfs(j)
for i in range(n):
    if not u[i]:
        p = []
        dfs(i)
        k = [t[i] for i in p]
        p.sort()
        k.sort()
        for i, j in enumerate(p):
            t[j] = k[i]
print(' '.join(map(str, t)))
